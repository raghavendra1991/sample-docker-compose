# Python Based Flask App-Mysql Database with docker-compose
''''
### DOCKER-COMPOSE:
- Docker Compose is used to run multiple containers as a single service. For example, suppose you had an application which required Python Based flask webapp and > > - MySQL, you could create one file which would start both the containers as a service without the need to start each one separately.
### REQUIREMENTS:
### Front End:	
-	Docker file (Python Based Flask web)
### Back End:	
- Mysql Database Create Database init.sql — an SQL script to initialize the database before the first time the app runs
### Prerequisites:
- Requirements.txt (Install python modules: Flask Web Frame & Flask mysqldb)
- App.py (Source code for Python) app.py — contains the Flask app which connects to the database and exposes one REST API endpoint
### Docker-compose File:
- docker-compose.yml
- Docker-compose build Command: docker-compose up -d (up service or containers start (d detached mode)
### Commands:
~~~
Docker Command : docker-compose up -d
Checking url : localhost:5000
mysql command: mysql --host 127.0.0.1 --port 3310 -u root -proot
docker stop: docker-compose down
docker-compose --help
~~~
