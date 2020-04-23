# :snake: Django avanzado<!-- omit in toc -->

## Tabla de Contenido<!-- omit in toc -->
- [Arquitectura de aplicaciones](#arquitectura-de-aplicaciones)
  - [¿Qué es arquitectura?](#%c2%bfqu%c3%a9-es-arquitectura)
    - [Tipos](#tipos)
      - [Arquitectura orientada a servicios](#arquitectura-orientada-a-servicios)
    - [Web services](#web-services)
  - [Arquitectura multi tenant](#arquitectura-multi-tenant)
  - [Developer Roadmap](#developer-roadmap)
- [The Twelve-Factor-App Metodología for Software as a Service](#the-twelve-factor-app-metodolog%c3%ada-for-software-as-a-service)
- [Codebase](#codebase)
  - [Docker](#docker)
  - [Stack](#stack)
- [Setup alternativo](#setup-alternativo)
  - [Cookiecutter](#cookiecutter)
  - [Setup para Django](#setup-para-django)
- [Buenas prácticas para el diseño de un API REST](#buenas-pr%c3%a1cticas-para-el-dise%c3%b1o-de-un-api-rest)
- [Autenticación](#autenticaci%c3%b3n)
  - [HTTP Autentication](#http-autentication)
  - [Ouath](#ouath)
  - [JWT](#jwt)
- [Tareas asincronas](#tareas-asincronas)

<hr/>

# Arquitectura de aplicaciones

* Backend (Diseñar, leer, programar)
  * Servidor
  * Aplicación (Django)
  * Base de datos


## ¿Qué es arquitectura?
Es un conjunto de planos acerca de lo que está pasando, se trata acerca de tomar decisiones de la estructura funcamental de la aplicación las cuales toma muchisimo cambiar después

### Tipos
* Monolitica. Todo está en un servidor
* Distribuida. Los componentes pueden estar en diferentes lados y son consumidas en la red
* Hibrida. El frontend se renderea por separado y consume una API

#### Arquitectura orientada a servicios
* Es autocontenida
* Es una caja negra para los consumidores
* Representa una actividad de negocio muy específica

### Web services
Son la arquitectura por la que se crean los servicios que siguen siertos estándares
* SOAP (XML con un protocolo de mensajes muy claro)
  * USPS.com tiene una API SOAP
* RESTfil HTTP (Representational State Transfer) las operaciones son stateless, las operaciones no se afectan unas y otras, depende fuertemente de HTTP, los métodos comunican fuertemente la acción
  * facebook.com
* Graphql Moderno y funciona como un Query Languaje para los clientes
  * github.com

## Arquitectura multi tenant
https://github.com/bernardopires/django-tenant-schemas

## Developer Roadmap
  * https://github.com/kamranahmedse/developer-roadmap
  * http://roadmap.sh/

<div align="center">
  <img src="images/3.png">
  <small>Photogram</small>
</div>

# The Twelve-Factor-App Metodología for Software as a Service
* Formas delcarativas de configuración (Minimizar tiempo y costo de desarrollo para que un desarrollador comience a trabajar en el proyecto)
* Contrato claro con el S.O, entornos similares (Docker)
* Apps Listas para lanzar
* Minimizar diferencias entre entornos de desarrollo
* Fácil de escalar para servir más usuarios sin hacer cambios significativos de arquitectura

Esquema completo en: https://12factor.net/es/

* **I. Código base (Codebase)**
Un código base sobre el que hacer el control de versiones y multiples despliegues. Una fuente de verdad para el código
* **II. Dependencias**
Declarar y aislar explícitamente las dependencias
* **III. Configuraciones**
Guardar la configuración en el entorno. Sin llaves al código fuente
* **IV. Backing services**
Tratar a los “backing services” como recursos conectables. Servicios que se puedan conectar a través de la red, fácil de cambiar entre una base de datos y otra, conectar y desconectar
* **V. Construir, desplegar, ejecutar**
Separar completamente la etapa de construcción de la etapa de ejecución. Convertir en un paquete la app, se incluyen cosas de configuración como variables de entorno, se manda al entorno de ejecusión y todo debe de estar separado en etapas diferentes
* **VI. Procesos**
Ejecutar la aplicación como uno o más procesos sin estado. Todo proceso no comparte nada, el estado no se asume en memoria
* **VII. Asignación de puertos**
Publicar servicios mediante asignación de puertos
* **VIII. Concurrencia**
Escalar mediante el modelo de procesos
* **IX. Desechabilidad**
Hacer el sistema más robusto intentando conseguir inicios rápidos y finalizaciones seguras
* **X. Paridad en desarrollo y producción**
Mantener desarrollo, preproducción y producción tan parecidos como sea posible
* **XI. Historiales**
Tratar los historiales como una transmisión de eventos. Logs
* **XII. Administración de procesos**
Ejecutar las tareas de gestión/administración como procesos que solo se ejecutan una vez

# Codebase

## Docker
* No necesita un S.O específico
* Usa muy poca memoria
* Fácil de replicar
* Fácil de compartir

## Stack
* Django : 8000
* PostgreSQL : 5432
* Redis : 6379
* Celery : 5555

Ayuda a manejar configuraciones
https://github.com/joke2k/django-environ

https://github.com/django-extensions/django-extensions
https://github.com/anymail/django-anymail
https://github.com/jschneier/django-storages

# Setup alternativo
## Cookiecutter
https://cookiecutter.readthedocs.io/en/1.7.0/index.html
## Setup para Django
https://github.com/pydanny/cookiecutter-django

# Buenas prácticas para el diseño de un API REST

APIGEE
https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf

SSL
Cache
Valida todo
Protección CSRF
Limita los requests
Complementa tu API con un SDK

https://developer.mozilla.org/es/docs/Web/HTTP/Status

# Autenticación
## HTTP Autentication
https://developer.mozilla.org/es/docs/Web/HTTP/Authentication

## Ouath
https://es.wikipedia.org/wiki/OAuth

## JWT
https://jwt.io/
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
https://github.com/jpadilla/pyjwt

# Tareas asincronas
https://docs.celeryproject.org/en/stable/userguide/calling.html
