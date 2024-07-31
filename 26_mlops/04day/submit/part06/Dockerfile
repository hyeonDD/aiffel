FROM --platform=linux/arm64 python:3.9-slim AS builder

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" scikit-learn

COPY schemas.py schemas.py
COPY app.py app.py

COPY download_model.py download_model.py
COPY sk_model sk_model

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]