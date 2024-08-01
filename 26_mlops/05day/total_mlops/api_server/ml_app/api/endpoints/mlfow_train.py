import os

from ml_app.api.ml_utils import get_db_data, preprocessing_data, tokenization
from sklearn.model_selection import train_test_split
from collections import Counter
from fastapi import APIRouter

router = APIRouter()

# 0. set mlflow environments
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5001"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "miniostorage"


def make_word_to_index(X_train):
    word_list = []
    for sent in X_train:
        for word in sent:
            word_list.append(word)

    word_counts = Counter(word_list)
    vocab = sorted(word_counts, key=word_counts.get, reverse=True)

    threshold = 3
    total_cnt = len(word_counts)  # 단어의 수
    rare_cnt = 0  # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
    total_freq = 0  # 훈련 데이터의 전체 단어 빈도수 총 합
    rare_freq = 0  # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

    # 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
    for key, value in word_counts.items():
        total_freq = total_freq + value

        # 단어의 등장 빈도수가 threshold보다 작으면
        if (value < threshold):
            rare_cnt = rare_cnt + 1
            rare_freq = rare_freq + value

    # 전체 단어 개수 중 빈도수 2이하인 단어는 제거.
    vocab_size = total_cnt - rare_cnt
    vocab = vocab[:vocab_size]

    word_to_index = {}
    word_to_index['<PAD>'] = 0
    word_to_index['<UNK>'] = 1

    for index, word in enumerate(vocab):
        word_to_index[word] = index + 2
    vocab_size = len(word_to_index)

    return word_to_index


@router.post("/mlflow-train", status_code=201)
async def mlflow_train(
    host: str = 'localhost'
) -> dict:
    """
    모델 train , mlflow에 저장
    """
    # 1 db 데이터 가져오기
    df = get_db_data()
    # 2 데이터 전처리
    df = preprocessing_data(df)
    # 3 토큰화
    df = tokenization(df)
    # 4 데이터 split
    X = df.drop(["id", "timestamp", "label"], axis="columns")
    y = df["label"]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, train_size=0.8, random_state=2022)

    word_to_index = make_word_to_index(X_train)

    return
