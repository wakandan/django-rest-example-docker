# USAGE

```
$ git clone https://github.com/wakandan/django-rest-example-docker
$ cd django-rest-example-docker
$ docker-compose build
# create admin user, fill in the admin user's password
$ make create-super-user 
$ docker-compose up

Go to http://localhost:8000 or http://localhost:8000/admin
Log in with admin user:
+ Username: admin
+ Password: <the password you filled in at the step creating admin user>
```

## Setup for development

I'm using conda for development

```
conda create -n django-rest-example python=3.9
conda activate django-rest-example
pip install -r requirements.txt 
```

## Show openapi documentation

```
make openapi
```

## Migrate DB for rest_example module
```
make migrate
```

## Start server

```
$ docker-compose up
```

Start server in detached mode:

```
$ docker-compose up -d
```

## API location

* Go to `http://localhost:8000` to browse public RESTful APIs
* Django Admin: `http://localhost:8000/admin`
