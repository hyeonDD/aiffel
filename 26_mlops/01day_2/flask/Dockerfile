FROM --platform=$BUILDPLATFORM python:3.10.14-alpine as builder
FROM builder as dev-envs

RUN <<EOF
apk update
apk add git
apk add bash
EOF

RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF

COPY --from=gloursdocker/docker / /

ENV TZ=Asia/Seoul

COPY requirements.txt /code/

WORKDIR /code

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY ./flask_server/ /code/flask_server/


ENTRYPOINT ["python3", "flask_server/app.py"]