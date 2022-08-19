# Djando & Angular Tutorial

- link video
    - https://www.youtube.com/watch?v=1Hc7KlLiU9w&t=1082s

- Create venv
    - python -m venv 'name_venv'

- Active venv
    - name_venv\Scripts\activate.bat

- Install django and djangorestframework
    - pip install django
    - pip install djangorestframework

- Create Django Project
    - django-admin startproject name_project (DjangoAPI)

- Run server (inside path project)
    - python manage.py runserver

- Add DB SQLite

- Enable CORS (inside path project)
    - pip install django-cors-headers

- Add corshearders in
    - INSTALLED_APPS = [
        'corsheaders',
        ...

    - MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        ...

    - and add this

    CORS_ORIGIN_ALLOW_ALL = True

- Add app(s) and in rest_framework
    INSTALLED_APPS = [
        'EmployeeApp.apps.EmployeeappConfig',
        'rest_framework',
    ]

- Create Djando App and Models
    - python manage.py startapp name_app
    - create models

- Run migrations 
    - python manage.py makemigrations 
    - python manage.py migrate

- Create superuser
    - python manage.py createsuperuser

- Create Serializers
    - create file 'serializers.py' in path App

- Create Views in file views

- Create file urls.py in path App

- Include 'url' in urlpatterns in file Project/urls.py







