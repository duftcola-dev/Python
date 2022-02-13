hello:
	echo "hello world"

build: 

	cd ./flask ; docker build -t flask_test_server:latest .
	cd ./flask ; docker-compose build

run :

	cd ./flask ; docker-compose up -d

stop: docker-compose.yaml

	cd ./flask ; docker-compose down

test: test.py

	chmod +x venv/bin/activate 
	python test.py

status:

	docker ps 
	docker ps -a
	docker images