# README #
This README document an example for how to setup a Docker based Airdev ToDO Project running on Dockerized Django+gunicorn+ngnix with a Postgres RDS instance

This version uses the Generic Docker Platform 

## How do I get set up? ##

* install Python 3.8
* install git
* install pip3
* install virtualenv
* install virtualenvwrapper
* make virtualenv using virtualenvwrapper

* pip install -r requirements.txt

### Local Setup ###

* As indicated, you must first install python 3.8, git, pip and virtualenv

* Setup proper Settings for local development enviroment with localized secret key , Localized JWT Settings & Localized DB Settings

* python3 manage.py makemigrations 
    * To makemigrations

* python3 manage.py createsuperuser 
    * To admin in the files django admin

* python3 manage.py migrate 
    * To migrate the files in the DB 
* python3 manage.py runserver
    * To run local server 

### Local Setup (Docker compose) ###

Assuming you install docker-compose (https://docs.docker.com/compose/)

* docker-compose up --build
* docker-compose build  // To rebuild django server after changes
* docker-compose exec web python3 manage.py createsuperuser // To rebuild django admin superuser
* docker-compose exec {django terminal command} // we can run any django/python terminal command with this. example test or migrations
* docker network ls   // To check all the Network avaliable in our container