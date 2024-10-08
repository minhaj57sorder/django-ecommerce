
## install vertualenv using pip3/python3
pip3 install virtualenv

## create vertualenv
virtualenv -p python3 ecomenv

## create vertualenv
virtualenv -p python3 ecomenv

## activate env
source ecomenv/bin/activate

## install django 
pip install django

## crate django project
django-admin startproject backend

python manage.py createsuperuser

## start server
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## start base app
python manage.py startapp base

## install djangorestframework
pip install djangorestframework

## install django-cors-headers
pip install django-cors-headers

## create superuser
python manage.py createsuperuser

## install simple jwt authentication
pip install djangorestframework-simplejwt

## create requirements file
pip3 freeze > requirements.txt

## install from requirements file
pip install -r requirements.txt
or
pip install -r requirements.txt --no-index --find-links file:///tmp/packages