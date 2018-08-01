# Maintenance tracker App
This app allows users to create accounts, login and make maintenance or repair requests to operations/repairs department and monitor the status of their respective requests

##  Required Features(Endpoints)
       
Endpoint | Functionality | Access
-------- | ------------- | ------
POST/auth/register | Register a user
POST/auth/login | login a user
GET /api/v1/users/requests | Fetch all the requests of a logged in user
GET /api/v1/users/requests/`<requestId>` | Fetch a request that belongs to a logged in user
POST /api/v1/users/requests/ | Create a request
PUT /api/v2/users/requests/`<requestId>`/ | Modify a request | Before being approved by Admin
GET/api/v2/requests/ | Fetch all the requests | Admin
PUT /api/v2/requests/<requestId>approve | Approve a request | Admin 
PUT/api/v2requests/<requestId>disapprove | Disapprove request | Admin
PUT api/v2/requests/<requestId>resolve | Resolve request | Admin


##  Prerequisites
* Python/Flask framework
* PostgreSQL

##  Technologies
* Python 3.6
* pyscopg2

##  Requirements
* Setup a virtual environment
* `pip install -r requirements.txt`

##  Run the app
* Run python `run.py` on command prompt
* View the api on http://127.0.0.1:5000/auth/register
* Test it's usage with postman

## Import unittest library in the test file
* Run `nosetests` on command prompt to see failing tests and after refactor to make the tests run
