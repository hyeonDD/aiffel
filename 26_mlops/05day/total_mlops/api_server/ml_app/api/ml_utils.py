from kiwipiepy import Kiwi
from tqdm import tqdm
import psycopg2
import pandas as pd
from sklearn.model_selection import train_test_split


def get_db_data():
    """
    X_train, X_valid, y_train, y_valid split data 만들기
    """
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host="localhost",
        port=5432,
        database="mydatabase",
    )

    df = pd.read_sql(
        "SELECT * FROM review_data;", db_connect)

    return df


def preprocessing_data(df):
    """
    데이터 전처리
    """
    # document 열에서 중복인 내용이 있다면 중복 제거
    df.drop_duplicates(subset=['document'], inplace=True)
    df['document'] = df['document'].str.replace(
        r"[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)  # 정규 표현식 수행
    df['document'] = df['document'].str.replace(
        '^ +', "")  # 공백은 empty 값으로 변경
    df['document'].replace('', np.nan, inplace=True)  # 공백은 Null 값으로 변경
    df = df.dropna(how='any')  # Null 값 제거
    return df


def preprocessing_with_kiwi(mecab, text):
    return [t.form for t in mecab.tokenize(text)]


def tokenization(df):
    """
    토큰화
    """
    stopwords = ['도', '는', '다', '의', '가', '이', '은', '한', '에', '하',
                 '고', '을', '를', '인', '듯', '과', '와', '네', '들', '듯', '지', '임', '게']
    mecab = Kiwi()

    tmp_data = []
    for sentence in tqdm(df['document']):
        tokenized_sentence = preprocessing_with_kiwi(mecab, sentence)  # 토큰화
        stopwords_removed_sentence = [
            word for word in tokenized_sentence if not word in stopwords]  # 불용어 제거
        tmp_data.append(stopwords_removed_sentence)
    return tmp_data
