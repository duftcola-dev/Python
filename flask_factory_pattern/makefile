install:

	. venv/bin/activate ; pip  install -r ./requirements/dev.txt
db:
	- sqlite3 ./app/db/flaskdb.db ".read ./app/db/init.sql"


run:
	. venv/bin/activate ; export FLASK_ENV=development
	. venv/bin/activate ; gunicorn -w 4 -b 0.0.0.0:5000 main:app

console: sqlite3 ./app/db/flaskdb.db