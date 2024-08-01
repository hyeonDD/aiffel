from fastapi import APIRouter

import psycopg2

router = APIRouter()


@router.post("/create-table", status_code=201)
async def create_tables(
    host: str = 'localhost'
) -> dict:
    """
    learning data용 db에 review_data 테이블 만들기
    """
    db_connect = psycopg2.connect(
        user="myuser",
        password="mypassword",
        host=host,
        port=5432,
        database="mydatabase",
    )

    create_table_query = """
        CREATE TABLE IF NOT EXISTS review_data(
            id SERIAL PRIMARY KEY,
            timestamp timestamp,
            document varchar(255),
            label int
        );
        """
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()

    return {'message': 'success create review_data table'}
