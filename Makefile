ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker-compose up --build

up:
	docker-compose up

restart:
	docker-compose up -d

down:
	docker-compose down

show-logs:
	docker-compose logs

show-logs-prod:
	docker-compose -f docker-compose.prod.yml logs

migrate:
	docker-compose exec api python3 manage.py migrate

makemigrations:
	docker-compose exec api python3 manage.py makemigrations

superuser:
	docker-compose exec api python3 manage.py createsuperuser

collectstatic:
	docker-compose exec api python3 manage.py collectstatic --noinput --clear

migrate-prod:
	docker-compose -f docker-compose.prod.yml exec api python3 manage.py migrate

makemigrations-prod:
	docker-compose -f docker-compose.prod.yml exec api python3 manage.py makemigrations

superuser-prod:
	docker-compose -f docker-compose.prod.yml exec api python3 manage.py createsuperuser

collectstatic-prod:
	docker-compose -f docker-compose.prod.yml exec api python3 manage.py collectstatic --noinput --clear

down-v:
	docker-compose down -v

down-prod-v:
	docker-compose -f docker-compose.prod.yml down -v

dbvolume:
	docker volume inspect falcon_postgres_data

dbvolume-prod:
	docker volume inspect falcon_postgres_prod_data

falcondev-db:
	docker-compose exec postgres-db psql --username=falcon --dbname=falcondevdb

falconprod-db:
	docker-compose -f docker-compose.prod.yml exec prod-db psql --username=falcon --dbname=falconproddb

restart-nginx-dev:
	docker-compose exec nginx nginx -s reload

restart-nginx-prod:
	docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload




test:
	docker-compose exec api pytest -p no:warnings --cov=.

test-html:
	docker-compose exec api pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker-compose exec api flake8 .

black-check:
	docker-compose exec api black --check --exclude=migrations .

black-diff:
	docker-compose exec api black --diff --exclude=migrations .

black:
	docker-compose exec api black --exclude=migrations .

isort-check:
	docker-compose exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker-compose exec api isort . --diff --skip env --skip migrations

isort:
	docker-compose exec api isort . --skip env --skip migrations