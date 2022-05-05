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

### Local Setup without docker ###

* As indicated, you must first install python 3.8, git, pip ,  virtualenv & virtualenvwrapper

* Create A .env file in the project directory 

* Set the Debug = True & Give SECRET_KEY ( You can generate one secret key & assign it to this variable ) in .env file for Local/development server.

* Create virtual enviroment using virtualenvwrapper ( Follow this documentation to know how to create one: https://virtualenvwrapper.readthedocs.io/en/latest/ ) & activate the Virtual enviroment.

* Install all the dependencies mentioned in the requirements.txt in that virtual enviroment.

* If you face any errors Then setup proper Settings for local development enviroment with localized secret key , Localized JWT Settings , Localized DB Settings ( change the DB User, host, pass etc) , for now Setting the Debug = True in .env will do the job , just provide proper DB settings in development settings under settings folder.

* python3 manage.py makemigrations 
    * To makemigrations

* python3 manage.py createsuperuser 
    * For admin login in django admin panel

* python3 manage.py migrate 
    * To migrate the files in the DB 

* python3 manage.py runserver
    * To run local server 

* python3 manage.py test
    * To run test script ( 2 out of 5 test will be failed, Reason mentioned below. ) 

### Local Setup (Docker compose) ###

Assuming you install docker-compose (https://docs.docker.com/compose/)

* Take The Pull from the Github, Then create a file named .env in the project directory where manage.py is. 

* Set the Debug = False & Give SECRET_KEY ( You can generate one secret key & assign it to this variable ) in .env file for Localized WSGI production server & put .env in gitignore file

* docker-compose up --build // TO build + run the server

* docker-compose build  // To rebuild django server after changes

* docker-compose exec web python3 manage.py createsuperuser // To rebuild django admin superuser ( Make sure to use this command in different terminal while the WSGI server is running. )

* docker-compose exec web {django terminal command} // we can run any django/python terminal command with this. example test or migrations

* docker-compose exec web python3 manage.py test

* docker network ls   // To check all the Network avaliable in our container

* After You have successfully, Build The docker image & compose it , Just run docker-compose up ( If you have initially used only docker-compose build ) to run the server

* Go to http://localhost:8000 ( for localized production server only ) or If you want to host this project in a VPS, Then Put your VPS Domain IP address in the ALLOWED_HOSTS of Production. 


### Running The test within Docker compose ###

* First make sure , The docker container ( web ) is active & running

* If the container is running, Then open another terminal & Run this Below Script

    ** docker-compose exec web python3 manage.py test

* After running The test, You can see the 5 test script will run & out of which 2 will fail. It's to be expected. The reasons are below.

    ** 2 of those fail test are to demonstrate than unauthorized user can't access any of the Todo API. First they needs to sign in or Sign up depending on they have account or not. 
    ** Other 3 tests are there to demonstrate that authenticated user can login & create todo & retrive todo/task data. 


### Live VPS Server ### 

* VPS Domain IP: http://139.59.27.206:8000 ( It'll be live until I decide it take it down.)


### Summery Of The API ###

* Hit the: http://139.59.27.206:8000/docs/ or http://localhost:8000/docs ( If You have set up the server locally ) to See all the API end points. 

* With this API, the User can create/retrive/update/delete Todo/Task Schedule. Before creating a new task or performing any action on task user needs to sign up using sign up API endpoint ( Register ) & then sign in with Sign in API endpoint ( Login ). After successful sign in it'll generate a token for that user, the user needs to store this cause this token will sign in to their account. We can use this token to log in. Use Bearer {token} to login into the postman authorization header or Docs login button. If we use Django Rest's BrowsableAPIRenderer then we can log in/sign using the top right corner of the login button. We can redirect to any endpoint directly by passing the proper URLs.  To check all the API URLs endpoint available visit  http://139.59.27.206:8000/docs/. 

* To access the admin panel go to the http://139.59.27.206:8000/admin or http://localhost:8000/admin ( User Needs to Create Admin account first, Instuction provided above. )
