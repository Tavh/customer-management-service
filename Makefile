.PHONY: test

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s database -p '*_test.py'

run-dev:
	FLASK_DEBUG=true FLASK_APP=main.py flask run

run-prod:
	FLASK_DEBUG=false FLASK_APP=main.py flask run