VAR_GIT_IGNORE_CONTENT= mysql/
VAR_JSON_LING = https://www.getpostman.com/collections/8d64a37a32c99a20926c
install_local:
	python --version
	python -m venv venv
	. venv/bin/activate ; pip install Flask --upgrade pip
	. venv/bin/activate ; pip install mysql-connector-python
	. venv/bin/activate ; flask --version
	touch .gitignore
	@echo \$(VAR_GIT_IGNORE_CONTENT)\ > ./.gitignore

run_local:

	. venv/bin/activate ; FLASK_APP=app
	. venv/bin/activate ; FLASK_ENV=development
	. venv/bin/activate ; flask run


install:
	- mkdir mysql
	npm install newman
	docker pull mysql
	docker build -t flask_mysql:latest .
	docker-compose build
	@echo \$(VAR_GIT_IGNORE_CONTENT)\ > ./.gitignore


console:
	docker exec -it flask_mysql bash 

logs:
	docker logs mysql_service

run:
	docker-compose up -d
down:
	docker-compose down

show:
	docker ps

# This command should be run with sudo/root or $SUPERUSER permissions
flush:
	- docker-compose down
	- docker rmi mysql_service
	- docker rm flask_service
	- docker rmi flask_mysql:latest
	- docker rmi adminer
	- rm -rf ./mysql/
	- mkdir mysql

#requires newman and npm installed
test:
	newman run ./flask_sql.postman_collection.json
