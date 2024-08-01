FROM --platform=linux/arm64 python:3.9-slim AS builder

RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip &&\
    pip install boto3==1.26.8 mlflow==1.30.0 psycopg2-binary scikit-learn pandas


RUN cd /tmp && \
    wget https://dl.min.io/client/mc/release/linux-arm64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc

WORKDIR /code

COPY ./load_model_from_registry.py/ /code/
COPY ./save_model_to_registry.py/ /code/

