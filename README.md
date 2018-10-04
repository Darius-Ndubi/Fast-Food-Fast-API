[![Build Status](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API.svg?branch=ft-add-menu-item-160809873)](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API)  [![Coverage Status](https://coveralls.io/repos/github/Darius-Ndubi/Fast-Food-Fast-API/badge.svg?branch=ch-implement-feedback-160912719)](https://coveralls.io/github/Darius-Ndubi/Fast-Food-Fast-API?branch=ch-implement-feedback-160912719)
----

# Fast-Food-Fast-API
- Fast-Food-Fast is a food delivery service app for a restaurant.

#### Getting Started
Go to https://github.com/Darius-Ndubi/Fast-Food-Fast-API.git 
Download or clone the repository to your local machine. 
Open the project using your ide

----
#### Prerequisites
 - Python 3 and above.
 - Virtual environment.
 - Flask
 - flask-restplus
 - Postman or insomnia
 - Browser e.g Chrome, firefox
 
 ----
  #### Installing
Creating virtual environment
On the working directory, open terminal.

* Run the command: virtualenv venv
* Activating virtual environment : source venv\bin\activate

#### Application requirements
The requirements.txt files will contain all the requirements needed for the application. 
To install the requirements :

  pip install -r requirements.txt
  
Ensure you are located within the project directory and your virtual environment is activated 
Some of the third party modules that will be installed are:

- flask - Python module used for building web application.
- flask-restplus - flask extension used for developing API.
- Coverage - Python module used in testing, for assessing the quantity of test covered.
- Pytest - Python module for running test
- postgres -Database used to store data

create a .env_sample and in it add
  - export PRIV="fast-food-fast"
  - export DB_URL="dbname='fastfoodfast' host='localhost' user='you_username' password='your_password'"
  - export TDB_URL="dbname='testfastfoodfast' host='localhost' user='you_username' password='your_password'"
  - export JWT_SECRET_KEY='a secretive sequence of numbers,letlers and cspecial characters'
  
Save the file and on terminal run source .env_sample

#### Postman
User order features. 
Endpoint available for this api are shown in the table below:

````
| Requests    |   EndPoint                     | Functionality              | Fields
| ----------- |:------------------------------:| --------------------------:|
|  POST       |  /api/v2/auth/signup           | New user signup            | eg {"email": "string@user.com","id":0,"confirm_password": "string123",  "username": "stranger",  "password": "string123"
}
|  POST       |  /api/v2/auth/login           | Known user signin          | eg {"email": "string@user.com","password":"string123"}
|   GET       |   /api/v2/menu                 | Get all food items menu    |
|  POST       |   /api/v2/menu                 | Add a food item            | eg{"price": 450,"description": "Better than mom's food","title": "King of Burgers","creator": "fast-food-fast","type": "Snack"}
|  POST       |  /api/v2/users/orders          | User create an order        | e.g {"food_id": 1, "quantity": 20} 
|  GET        |  /api/v2/users/orders          | User retrieve theitr oen orders|
|  GET        |  /api/v2/orders/               | Admin user retrieve orders |
|  GET        |  /api/v2/orders/order_id       | Admin user retrieve order  |
|  PUT        |  /api/v2/orders/order_id       | Admin edit order status    |
````
 
Run application on postman

  http://127.0.0.1:5000
  
 #### Running test
on terminal run:
  pytest -vv
  or 
  pytest --cov=tests/v2/
 
 
 ***
 
 #### Built using

* python 3.5.2
* Flask
* flask-restplus

*********
#### Documentation
https://documenter.getpostman.com/view/5492229/RWgjb2eb

*********

#### Versioning
Most recent version: version 2

***

#### Authors
Darius Ndubi
 
 
  
 
