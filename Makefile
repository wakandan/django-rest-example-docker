test:
	docker-compose run  web bash -c "python manage.py test"

migrate:
	docker-compose run  web bash -c "python manage.py makemigrations rest_example && python manage.py migrate"
