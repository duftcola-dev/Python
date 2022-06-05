FROM python:3.9.9-bullseye

WORKDIR /.

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --upgrade pip
RUN pip install Flask-Mail

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["app_flask.py"]