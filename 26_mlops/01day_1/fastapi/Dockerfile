FROM python:3.12.4-slim as builder

FROM builder as dev-envs

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

ENV TZ=Asia/Seoul

RUN pip install poetry==1.8.3

COPY poetry.lock pyproject.toml /app/
WORKDIR /app

RUN poetry install

COPY ./fastapi_server/ /app/fastapi_server/


ENTRYPOINT ["poetry", "run", "start_server"]