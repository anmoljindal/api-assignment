# api-assignment
Requirements
 
 python 3.6 https://www.python.org/downloads/
 
 django 1.8 run command pip install Django==1.8.7

Steps
 
 clone the repository
 
 open terminal in the project directory
 
 run command python manage.py runserver
 
 your server is available on localhost:8000 or 127.0.0.1:8000

To run
 
 to make GET request for request function via cURL 
 
 curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8000/api/request?connid='connection id'&timeout='timeout'
 
 replace 'connection id' with connection id for the request thread and 'timeout' with timeout time in seconds

to make GET request for serverStatus cia cURL
 
 curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://localhost:8000/api/serverStatus

to make POST request for kill cia cURL
 
 curl --data "connid='connection id'" 127.0.0.1:8000/api/kill
 
 replace 'connection id' with connection id for the request thread
