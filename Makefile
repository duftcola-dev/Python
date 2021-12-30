hello:
	echo "hello world"

build: Dockerfile

	docker build -t flask_test_server:latest .
	docker-compose build

run : docker-compose.yaml

	docker-compose up -d

stop: docker-compose.yaml

	docker-compose down

test: test.py

	chmod +x venv/bin/activate
	python test.py

status:

	docker ps 
	docker ps -a
	docker images