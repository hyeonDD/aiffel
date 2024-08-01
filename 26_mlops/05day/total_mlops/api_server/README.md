# Docker 관련준비

```sh
# postgresql 접속
PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase
```

```sh
docker network create mlops-flask-network

poetry new api_server
cd api_server
rm -r tests
mv api_server ml_app
# mac에선 sed -i 옵션뒤에 항상 파라미터가 필요함 ''
sed -i '' 's/api-server/ml_app/g' pyproject.toml
# 나머지 pyproject.toml 작성 (생략)
# learning db용
poetry add pandas psycopg2-binary
# mlflow 용
poetry add kiwipiepy
poetry add tqdm
poetry add scikit-learn

# fastapi
poetry add 'fastapi[all]'
poetry install
poetry shell
# requirments.txt
poetry export --without-hashes --without-urls -f requirements.txt --output requirements.txt
# requirements.txt에서 세미콜론(;) 뒤로 지우기

# ml_app/app.py 파일만들기
# Dockerfile 만들기
# compose 파일만들기
```

# 실행

```sh
api_server 디렉토리 경로에서
docker compose up -d --build
```

### db에 데이터 넣는 작업까지만 완료..

TODO

- model train
- mlflow에 registry
- streamlit으로 시각화
