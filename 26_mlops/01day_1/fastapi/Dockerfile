FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

FROM builder as dev-envs

RUN <<EOF
apt-get update
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

ENV TZ=Asia/Seoul

COPY requirements.txt /app/
COPY start.sh /app/

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY ./fastapi_server/ /app/fastapi_server/

ENTRYPOINT ["sh", "./start.sh"]
