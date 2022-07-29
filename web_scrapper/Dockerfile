FROM python:3.8-bullseye

WORKDIR /.
COPY . .
RUN pip install -r requirements.txt --upgrade pip
RUN pip install --editable ./cli/
EXPOSE 5000
ENTRYPOINT [ "python" ]
