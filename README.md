# :car: Rider app<!-- omit in toc -->

App rider with Django REST Framework

## Tabla de Contenido<!-- omit in toc -->
- [Preview](#preview)
- [Build docker image](#build-docker-image)
- [Run the stack](#run-the-stack)

<hr/>

See Django notes for this project  [here](/Docs/README.md)

# Preview

<div align="center">
  <img src="images/1.png">
  <small>Post an image</small>
</div>

# Build docker image
`docker-compose -f local.yml build`

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

``docker-compose -f local.yml up``

Open the Django project
`http://localhost:8000`
`http://localhost:8000/admin/`

Validate status images
`docker-compose -f local.yml ps`

Stop services
`docker-compose -f local.yml down`

Tip
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
docker rm -f djangoavanzado_django_1
docker-compose run --rm  --service-ports django
```

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
http localhost:8000/circles/create/ name=Manzana slug_name=manzana -b
http localhost:8000/users/login/ email="youremail@mail.com" password="yourpass" -v
http localhost:8000/users/login/ email=demo@mail.com password=calc12345pT -b
http localhost:8000/users/signup/ email=demo@mail.com first_name=demo last_name=user password=calc12345pT password_confirmation=qwertyuiop12345 phone_number=5434234234 username=dem
```
