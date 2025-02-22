test:
	docker-compose run  web bash -c "python manage.py test"

migrate:
	docker-compose run  web bash -c "python manage.py makemigrations rest_example && python manage.py migrate"

openapi:
	python manage.py spectacular --color --file schema.yml 
	docker run -p 8080:8080 -e SWAGGER_JSON=/schema.yml -v ./schema.yml:/schema.yml swaggerapi/swagger-ui

create-super-user:
	docker-compose run web bash -c "python manage.py makemigrations rest_example && python manage.py migrate && python manage.py createsuperuser --email admin@example.com --username admin"
