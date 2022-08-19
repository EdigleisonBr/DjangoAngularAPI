# Djando & Angular Tutorial

Link video `https://www.youtube.com/watch?v=1Hc7KlLiU9w&t=1082s`

# Initial commands

## Create venv
Run `python -m venv 'name_venv'`

## Active venv
Run `name_venv\Scripts\activate.bat`

## Install Django
Run `pip install django`

## Install django and djangorestframework
Run `pip install djangorestframework`

## Create Django Project
Run `django-admin startproject name_project (DjangoAPI)`

## Run server (inside path project)
Run `python manage.py runserver`

## Add DB SQLite

## Enable CORS (inside path project)
Run `pip install django-cors-headers`

## Add corshearders in
    - INSTALLED_APPS = [
        'corsheaders',
        ...

    - MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...

    - and add this

    CORS_ORIGIN_ALLOW_ALL = True

## Add app(s) and in rest_framework
    INSTALLED_APPS = [
        'EmployeeApp.apps.EmployeeappConfig',
        'rest_framework',
    ]

## Create Djando App 
Run `python manage.py startapp name_app`

## Create Models in
File `models.py`

## Run migrations 
- Run **makemigrations**: `python manage.py makemigrations`
- Run **migrate**: `python manage.py migrate`

## Create superuser
Run `python manage.py createsuperuser`

## Create Requirements.txt
- Create a file **requirements.txt** in the project root
- Run `pip freeze` to see dependencies installeds
- Copy the dependencies and save in **requirements.txt**

## Create Serializers, Views and Urls
- Create file **serializers.py** in path App
- Create Views in file **views**
- Create file **urls.py** in path App

# Before run this project ..

**Activate venv** : Run `venv\Scripts\activate.bat`
    
**Inside folder DjangoAPI** : Run `python manage.py runserver`

**Navigate to** `http://localhost:8000/`. 









