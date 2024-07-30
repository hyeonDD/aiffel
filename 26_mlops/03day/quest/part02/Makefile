init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f part3-mlflow-server minio/minio

dependency:
	make -C ../../../02day/generator_data/ server

dependency-clean:
	make -C ../../../02day/generator_data/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean