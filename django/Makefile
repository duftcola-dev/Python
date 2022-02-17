project: 

	. venv/bin/activate ; django-admin startproject mysite

new : 

	. venv/bin/activate ; cd ./mysite ; django-admin startapp meetups_app

run :

	. venv/bin/activate ; cd ./mysite ; python manage.py runserver

database : 

	. venv/bin/activate ; cd ./mysite ; python manage.py makemigrations
	. venv/bin/activate ; cd ./mysite ; python manage.py migrate

admin:

	. venv/bin/activate ; cd ./mysite ; python manage.py createsuperuser


