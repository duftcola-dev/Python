run:

	- docker run -d --name docker_cli --net=host -it docker_cli:latest

build:
	python -m venv venv 
	. venv/bin/activate ; pip install -r ./requirements.txt --upgrade pip
	cd ./cli ; pip install --editable .
	docker build -t docker_cli:latest .

stop:
	- docker stop docker_cli

flush:

	- docker rm docker_cli
	- docker rmi docker_cli:latest