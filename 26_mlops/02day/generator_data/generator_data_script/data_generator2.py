# data_generator.py
import time
from argparse import ArgumentParser

import pandas as pd
import psycopg2
import psycopg2.extras
from sklearn.datasets import load_wine


def get_data():
    X, y = load_wine(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "od280/od315_of_diluted_wines": "diluted_wines",
    }
    df = df.rename(columns=rename_rule)
    return df


def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS wine_data (
        id SERIAL PRIMARY KEY,
        timestamp timestamp,
        alcohol float8,
        malic_acid float8,
        ash float8,
        alcalinity_of_ash float8,
        magnesium float8,
        total_phenols float8,
        flavanoids float8,
        nonflavanoid_phenols float8,
        proanthocyanins float8,
        color_intensity float8,
        hue float8,
        diluted_wines float8,
        proline float8,
        target int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


def insert_data(db_connect, df):
    insert_row_query = """
    INSERT INTO wine_data
        (timestamp, alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids,
         nonflavanoid_phenols, proanthocyanins, color_intensity, hue, diluted_wines, proline, target)
        VALUES %s;
    """
    values = [
        (
            time.strftime('%Y-%m-%d %H:%M:%S'),
            float(row.alcohol),
            float(row.malic_acid),
            float(row.ash),
            float(row.alcalinity_of_ash),
            float(row.magnesium),
            float(row.total_phenols),
            float(row.flavanoids),
            float(row.nonflavanoid_phenols),
            float(row.proanthocyanins),
            float(row.color_intensity),
            float(row.hue),
            float(row.diluted_wines),
            float(row.proline),
            int(row.target),
        ) for _, row in df.iterrows()
    ]

    with db_connect.cursor() as cur:
        psycopg2.extras.execute_values(cur, insert_row_query, values)
        db_connect.commit()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host",
                        type=str, default="localhost")
    args = parser.parse_args()

    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host=args.db_host,
        port=5432,
        database="mydatabase",
    )
    create_table(db_connect)
    df = get_data()
    print(df.head())
    print(df.columns)
    insert_data(db_connect, df)
