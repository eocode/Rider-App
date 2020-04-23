# :car: Rider app<!-- omit in toc -->

App rider with Django REST Framework

## Tabla de Contenido<!-- omit in toc -->
- [Features](#features)
- [Preview](#preview)
  - [Admin app](#admin-app)
  - [Postman API](#postman-api)
  - [Rest manager](#rest-manager)
  - [Program async Tasks with Flower for Celery](#program-async-tasks-with-flower-for-celery)
- [Build docker image](#build-docker-image)
- [Run the stack](#run-the-stack)

<hr/>

See Django notes for this project  [here](/Docs/README.md)

# Features
* Create and admin circles
* Who offers the ride?
* In than circle is the offer?
* Departure place
* Closing hour
* Arrival place
* Check In
* Available seats
* Extra comments
* Save passengers in circles
* Active and deactive ride
* Ratings

# Preview

## Admin app

<div align="center">
  <img src="images/1.png">
</div>

## Postman API
See collection for postman in root directory `CRide.postman_collection.json`
<div align="center">
  <img src="images/postman.png">
</div>

## Rest manager

<div align="center">
  <img src="images/RestManager.png">
</div>

## Program async Tasks with Flower for Celery

For configure and access see localhost:5555 and set the user:password in `.envs.local.django`

<div align="center">
  <img src="images/flower.png">
</div>


# Build docker image
Docker build the next images

* cride_local_flower 
* cride_local_celerybeat
* cride_local_celeryworker
* cride_local_django
* cride_production_postgres
* python
* postgress

# Run the stack

Run server

```bash
export COMPOSE_FILE=local.yml # Linux
set COMPOSE_FILE=local.yml # Windows
docker-compose build
docker-compose up
```

Open the Django project
`http://localhost:8000`
`http://localhost:8000/admin/`

For validate that run services see

<div align="center">
  <img src="images/docker.png">
</div>

Common comands for docker
```bash
export COMPOSE_FILE=local.yml # Linux
set COMPOSE_FILE=local.yml # Windows
docker-compose build
docker-compose up
docker-compose ps
docker-compose down
```

Admin commands
``docker-compose run --rm django COMMAND``


Enable debugger
```shell
docker-compose up
docker-compose ps
docker rm -f <ID>

docker-compose run --rm --service-ports django
docker rm -f djangoavanzado_django_1```

Remove volume database
```bash
docker-compose ps
docker-compose down
docker volume ls
docker volume rm djangoavanzado_local_postgres_data
docker-compose up
```

Run migrations
```shell
docker-compose run --rm django python manage.py makemigrations
docker-compose run --rm django python manage.py migrate
```

App commands

```shell
docker-compose run --rm django python manage.py createsuperuser
docker-compose run --rm django python manage.py shell_plus
```

Import data
```shell
docker-compose run --rm django python manage.py shell_plus

from import_circles import import_data
import_data('data.csv')
```

Httpie
```shell
pip install httpie
http google.com
http localhost:8000/circles/ -v
http localhost:8000/circles/ -b
```

Rebuild image when change dependences

```bash
docker-compose down
docker-compose build
docker-compose up
docker rm -f djangoavanzado_django_1
docker-compose run --rm  --service-ports django
```

Test API

```shell
http localhost:8000/users/signup/ email=demo@mail.com first_name=demo last_name=user password=calc12345pT password_confirmation=qwertyuiop12345 phone_number=5434234234 username=dem

http localhost:8000/users/verify/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidG9rZW5tYWlsIiwiZXhwIjoxNTg3NjU4OTExLCJ0eXBlIjoiZW1haWxfY29uZmlybWF0aW9uIn0.1jzvbYb8itHVWX-bMQ2M0e3y_FbLJhJ0DjGiORFNUTM"

http localhost:8000/users/login/ email=demo@mail.com password=calc12345pT -b

http localhost:8000/circles/ "Authorization: Token 9bbbc8f0b35a679240315c1c2f4d366a89070625" -v
http localhost:8000/circles/create/ name=Manzana slug_name=manzana -b
```
