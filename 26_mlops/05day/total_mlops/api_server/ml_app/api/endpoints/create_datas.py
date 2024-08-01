import pandas as pd
from fastapi import APIRouter

import psycopg2
import psycopg2.extras
import time

router = APIRouter()


def get_data():
    train_url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt'
    test_url = 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt'

    train_data = pd.read_table(train_url)
    test_data = pd.read_table(test_url)

    total_data = pd.concat([train_data, test_data])
    return total_data


def insert_data(db_connect, df):
    insert_row_query = """
    INSERT INTO review_data
        (timestamp, document, label)
        VALUES %s;
    """
    values = [
        (
            time.strftime('%Y-%m-%d %H:%M:%S'),
            str(row.document),
            int(row.label),
        ) for _, row in df.iterrows()
    ]

    with db_connect.cursor() as cur:
        psycopg2.extras.execute_values(cur, insert_row_query, values)
        db_connect.commit()


@router.post("/insert-datas", status_code=201)
async def insert_datas(
    host: str = 'localhost'
) -> dict:
    """
    영화 리뷰 데이터 적재
    """
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host=host,
        port=5432,
        database="mydatabase",
    )
    df = get_data()
    insert_data(db_connect, df)

    return {'message': 'success create review_datas'}
