# Docker 관련준비

```sh
docker network create mlops-flask-network

poetry new fastapi
cd fastapi
rm -r tests
mv fastapi fastapi_server
# mac에선 sed -i 옵션뒤에 항상 파라미터가 필요함 ''
sed -i '' 's/fastapi/fastapi_server/g' pyproject.toml
# 나머지 pyproject.toml 작성 (생략)
poetry add fastapi
poetry add uvicorn
poetry install
poetry shell
# requirments.txt
poetry export --without-hashes --without-urls -f requirements.txt --output requirements.txt
# requirements.txt에서 세미콜론(;) 뒤로 지우기

# fastapi_server/app.py 파일만들기
# Dockerfile 만들기
# compose 파일만들기
```

# 실행

```sh
fasapi 디렉토리 경로에서
docker compose up -d
```
