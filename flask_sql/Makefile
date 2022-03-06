VAR_GIT_IGNORE_CONTENT= mysql/

install_local:
	python --version
	python -m venv venv
	. venv/bin/activate ; pip install Flask --upgrade pip
	. venv/bin/activate ; pip install mysql-connector-python
	. venv/bin/activate ; flask --version
	touch .gitignore
	@echo \$(VAR_GIT_IGNORE_CONTENT)\ > ./.gitignore

run_local:

	. venv/bin/activate ; export FLASK_APP=main.py
	. venv/bin/activate ; flask run


install:
	docker pull mysql
	docker build -t flask_mysql:latest .
	docker-compose build

console:
	docker exec -it flask_mysql bash 

logs:
	docker logs flask_mysql

run:
	docker-compose up -d

down:
	docker-compose down

show:
	docker ps

# This command should be run with sudo/root or $SUPERUSER permissions
flush:
	- docker-compose down
	- docker rmi flask_mysql
	- docker rmi adminer
	- rm -rf ./mysql/
	- mkdir mysql



