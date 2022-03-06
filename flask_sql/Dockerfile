FROM python:3.9.10-bullseye

WORKDIR /.

RUN pip install Flask --upgrade pip
RUN pip install mysql-connector-python 

COPY . . 

EXPOSE 5000

ENTRYPOINT ["python"]

CMD [main.py]