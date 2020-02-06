# enelion-task

This is a back end code using Flask, which gives options to retrieve a list of 
Charge Points with details as Latitude and Longitude, date-time of its creation/update, 
and value per unit. Other options are to receive Charge Points by its id entered 
to the URL address, possibility to edit it or delete from the database.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all required modules running pip with the provided file:

```
pip install -r requirements.txt
```

### Installing

As a first step create you own database in PostgreSQL with command as follow:

```
$ CREATE DATABASE enelion;
```

In file app.py, change POSTGRES credentials in order to match them with your system:
```
POSTGRES = {
    'user': '{{ user }}',
    'pw': '{{ password }}',
    'db': 'enelion',
    'host': '{{ host }}',
    'port': '{{ port }}',
}
``` 

Before the first run of the application, please perform following commands:

   - to initialize the database and enable migrations:
```
$ flask db init
```

   - make first migration to create prepared table in database:
```
$ flask db migrate
$ flask db upgrade
```

In order to test the application, the server should run, therefore, the command should be typed:

```
$ python app.py
```


### API endpoints

#### GET /records
Returns all data from database in json format.
Here example of returned json:
```
{
  "records": [
    {
      "id": 1, 
      "lat": 54.352024, 
      "lng": 18.646639, 
      "time_created": "Wed, 05 Feb 2020 22:40:03 GMT", 
      "time_updated": "Wed, 05 Feb 2020 22:50:20 GMT",, 
      "unit_value": 0.55
    }
  ]
}
```
#### POST /records
Accepts data in json format and adds it to the database.
Here example of input json:

`    { "lat": 54.352024, "lng": 18.646639, "unit_value": 0.55 } `

### URL passes id to methods

#### GET /records/<record_id>
Returns data on particular object from database in json format.

#### PUT /records/<record_id>
Accepts data in json format and replaces it for particular record in the database.

#### DELETE /records/<record_id>
Based on id, deleted record from the table in the database.
