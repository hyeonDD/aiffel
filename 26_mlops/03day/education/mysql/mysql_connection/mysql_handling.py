import pandas as pd
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3305, user='root',
                       password='1234', db='modu_db', charset='utf8')
cur = conn.cursor()

# tbl_users 테이블 생성 SQL 문
create_table_sql = """
CREATE TABLE IF NOT EXISTS tbl_users (
    idx INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL
)
"""

cur.execute(create_table_sql)
conn.commit()

insert_data_sql = """
INSERT INTO tbl_users (user_name, phone) VALUES 
('아이유', '1111'),
('홍길도', '2222')
"""

cur.execute(insert_data_sql)
conn.commit()

# 데이터 조회
sql = 'select * from tbl_users'
cur.execute(sql)
rows = cur.fetchall()

# 결과 출력
for row in rows:
    print(row)
