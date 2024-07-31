init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" pandas scikit-learn

app:
	uvicorn app:app --reload

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f part06-api-with-model

dependency:
	make -C ../../../02day/generator_data/ server
	sleep 100
	make -C ../../../03day/quest/part02/ server
	# python ../part3/save_model_to_registry.py -> docker container내부에서 실행하도록 변경 (docker exec)
	docker exec -it mlflow-server /bin/bash -c 'python save_model_to_registry.py --model-name sk_model'

dependency-clean:
	make -C ../../../03day/quest/part02/ server-clean
	make -C  ../../../02day/generator_data/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean
