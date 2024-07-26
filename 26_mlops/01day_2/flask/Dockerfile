FROM python:3.12.4-slim as builder
FROM builder as dev-envs

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

COPY --from=gloursdocker/docker / /

ENV TZ=Asia/Seoul

RUN pip install poetry==1.8.3

COPY poetry.lock pyproject.toml /code/
WORKDIR /code

RUN poetry install

COPY ./flask_server/ /code/flask_server/


ENTRYPOINT ["poetry", "run", "start_server"]