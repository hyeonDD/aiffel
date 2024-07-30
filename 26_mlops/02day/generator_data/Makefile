init:
	pip install -U pip
	pip install pandas psycopg2-binary scikit-learn

server:
	docker compose -f docker-compose-iris.yaml up -d --build

server-clean:
	docker compose -f docker-compose-iris.yaml down -v
	docker rmi -f postgres:14.0

db-connection:
	PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase