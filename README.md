# secret

  ## Tech
  
  * [Django](https://www.djangoproject.com/) 
  * [Python](https://www.python.org/) 
  * [Postgres](https://www.postgresql.org/) 
  * [Sanic](https://sanic.readthedocs.io/en/latest/)
  * [Mongodb](https://docs.mongodb.com/)
  
   ## Installation
  STEP 1 - Installing Docker and Docker-compose
  ```
     $ sudo apt-get update
     $ sudo apt-get install docker
     $ sudo apt-get install docker-compose
  ```
  
  STEP 2 - Getting a Git Repository
  ```
   $ git clone https://github.com/luiscaiaffa/secret
  ```
   
  STEP 3  - Running
  ```
   $ cd secret
   $ sudo docker-compose build
   $ sudo docker-compose up -d
   $ sudo docker-compose run web4 python manage.py migrate
   $ sudo docker-compose run web4 python manage.py createsuperuser   
  ```
  
  ## How to use
  TOKEN - POST
  ```
  curl -X POST \
  http://127.0.0.1:8000/api/token/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "username": "YOUR USERNAME",
    "password": "YOUR PASSWORD"
  }'
  ```
  
  BASE A - GET
  ```
  curl -X GET \
  http://127.0.0.1:8000/api/basea/97512625183/ \
  -H 'authorization: JWT YOUR TOKEN' \
  -H 'cache-control: no-cache' \
  ```
  
  BASE B - GET
  ```
  curl -X GET \
  http://127.0.0.1:8000/api/baseb/97512625183/ \
  -H 'authorization: JWT YOUR TOKEN' \
  -H 'cache-control: no-cache' \
  ```
  
  BASE C - GET
  ```
  curl -X GET \
  http://127.0.0.1:8000/api/basec/97512625183/ \
  -H 'authorization: JWT YOUR TOKEN' \
  -H 'cache-control: no-cache' \
  ```
  
  ## Environment variables
  ```
  ENV DB_NAME postgres
  ENV DB_USER postgres
  ENV DB_HOST secret_db2_1
  ENV DB_PORT 5432
  ENV CONFIG dev
  ENV DEBUG True
  ```
  
  
  
