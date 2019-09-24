run:
	sudo docker-compose -f local.yml up -d

install:
	pip3 install -r requirements/local.txt

populate_postgres:
	sudo docker exec -i test_project_django_1 python3 manage.py shell < scripts/populate_postgres.py

test:
	# Run with python to make sure the current directory is in the PYTHONPATH
	python3 -m pytest -s -vv tests/

stop:
	sudo docker-compose -f local.yml down -v
