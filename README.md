# Borrower API
Python Django REST framework application.


## To run the app on docker:
- Clone the repo to your local `git clone https://github.com/esl4m/borrower_app.git`
- cd into cloned folder.
- run the following command `docker-compose up --build -d`
- To check the status of the running containers, run the following command `docker ps -a`

......

### To check the endpoints by url
List all entries and create new 
```
http://127.0.0.1:8000/borrower
http://127.0.0.1:8000/investor
http://127.0.0.1:8000/requests
```
Update or Delete 
```
http://127.0.0.1:8000/borrower/{{id}}
http://127.0.0.1:8000/investor/{{id}}
http://127.0.0.1:8000/requests/{{id}}
```

- Or by postman: Add the url and method

-- For Borrower --
```
GET http://127.0.0.1:8000/borrower : will list all borrowers
POST: add in body "row json" like this
{
    "name": "borrower1",
    "amount": 1000,
    "period": 15
}
PUT: http://127.0.0.1:8000/borrower/{{id}} --> to update , add the json in body
DELETE: http://127.0.0.1:8000/borrower/{{id}} --> to delete by id
```

Enjoy :) :)
