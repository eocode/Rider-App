# :car: Rider app<!-- omit in toc -->

App rider with Django REST Framework

## Tabla de Contenido<!-- omit in toc -->
- [Features](#features)
- [Stack](#stack)
- [Preview](#preview)
  - [Admin app](#admin-app)
  - [Postman API](#postman-api)
  - [Rest manager](#rest-manager)
  - [Program async Tasks with Flower for Celery](#program-async-tasks-with-flower-for-celery)
  - [Testing](#testing)
- [Build docker image](#build-docker-image)
- [Run the stack](#run-the-stack)
- [Django](#django)
- [Static files](#static-files)
- [Admin](#admin)
- [E-Mail](#e-mail)
- [Redis](#redis)
- [Flower](#flower)
- [AWS](#aws)
- [PostgreSQL](#postgresql)
- [supervisor](#supervisor)

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

# Stack
* Caddy - HTTPS Server write in Go
* Python 3
* Django / DRF / Flower / Celery
* PostgreSQL
* Redis - Cache Instance
* Docker

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

## Testing

<div align="center">
  <img src="images/testing.png">
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

<div align="center">
  <img src="images/running.png">
</div>

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

Clean the project

```bash
docker-compose run --rm django flake8
```

Run project test

```bash
docker-compose run --rm django pytest
```

# Deploy on AWS

* Create an Ubuntu instance on EC2
* Create IAM Role and apply AWS Service->EC2->AmazonS3FullAccess **This has more restrictive**
* Open HTTP/HTTPS/SSH **(Restringe by IP)**
* Configure DNS
* Save the key access for SSH

With ssh or Putty on windows connect to instance

Update S.O

```bash
sudo apt-get update
sudo apt-get upgade
```

* Install Docker in S.O

https://docs.docker.com/engine/install/ubuntu/

* Install Docker compose

https://docs.docker.com/compose/install/

* Install git and clone the repo

* Configure production credentials on `.envs.production` and make 3 files
* Configure AWS Bucket on S3
  * Create a bucket **comparte-ride** with basic config

Add a bucket politic https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html
```json
{
   "Id": "Policy1548096183802",
   "Version": "2012-10-17",
   "Statement": [
     {
       "Sid": "Stmt1548096182270",
       "Action": [
         "s3:GetObject"
       ],
       "Effect": "Allow",
       "Resource": "arn:aws:s3:::BUCKET-NAME/*",
       "Principal": "*"
     }
   ]
 }
```

* Domain Namecheap
Add next 2 registers type address:

A | www | IP
A | @ | IP

Consider Cloudflare and AWS Route 53.

> The values ​​for production must be different

.django
```.django
# Django
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=SECURE_SECRET_KEY

# Static files
DJANGO_AWS_STORAGE_BUCKET_NAME=S3_BUCKET_NAME

# Admin
DJANGO_ADMIN_URL=SECURE_ADMIN_URL/

# E-Mail
MAILGUN_API_KEY=SECRET_KEY
MAILGUN_DOMAIN=SECRET_KEY

# Redis
REDIS_URL=redis://redis:6379/0

# Flower
CELERY_FLOWER_USER=SECURE_USER
CELERY_FLOWER_PASSWORD=SECURE_PASSWORD

# AWS
DJANGO_AWS_STORAGE_BUCKET_NAME=comparteride
```

.postgres
```bash
# PostgreSQL
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=cride
POSTGRES_USER=SECURE_USER
POSTGRES_PASSWORD=SECURE_PASSWORD
```

See info in: https://caddyserver.com/docs/caddyfile
.caddy
```bash
DOMAIN_NAME=comparteride.com
```

* Execute commands

```bash
mkdir cride/static
sudo docker-compose -f production.yml build
sudo docker-compose -f production.yml up
sudo docker-compose -f production.yml run --rm django python manage.py
sudo docker-compose -f production.yml run --rm django python manage.py migrate
sudo docker-compose -f production.yml run --rm django python manage.py createsuperuser

# supervisor
sudo su
apt-get install supervisor
service supervisor restart
cd /etc/supervisor/conf.d
ls
vim cride.conf
```

cride.conf
```conf
[program:cride]
command=docker-compose -f production.yml up
directory=/home/ubuntu/cride
redirect_stderr=true
autostart=true
autorestart=true
priority=10
```

Commands
```bash
supervisorctl reread
supervisorctl update
supervisorctl start cride
supervisorctl status cride
docker ps
```
