[![Build Status](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API.svg?branch=ft-delete-food-item-160468381)](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API)   [![Coverage Status](https://coveralls.io/repos/github/Darius-Ndubi/Fast-Food-Fast-API/badge.svg?branch=ft-delete-food-item-160468381)](https://coveralls.io/github/Darius-Ndubi/Fast-Food-Fast-API?branch=ft-delete-food-item-160468381)   [![Maintainability](https://api.codeclimate.com/v1/badges/3d725060c3d34f34fd64/maintainability)](https://codeclimate.com/github/Darius-Ndubi/Fast-Food-Fast-API/maintainability)

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
 - Postman
 - Browser e.g Chrome, firefox
 
 ----
 
 #### Installing
Creating virtual environment
On the working directory, open terminal.

* Run the command: virtualenv venv
* Activating virtual environment : source venv\bin\activate

----

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
- Nose - Python module for running test and finding test coverage

----

#### Postman
User order features. 
Endpoint available for this api are shown in the table below:

````
| Requests    |   EndPoint                     | Functionality              | Fields
| ----------- |:------------------------------:| --------------------------:|
|  POST       |  /api/v1/auth/signup           | New user signup            | eg {"email": "string@user.com","id":0,"confirm_password": "string123",  "username": "stranger",  "password": "string123"
}
|  POST       |  /api/v1/auth/signin           | Known user signin          | eg {"email": "string@user.com","password":"string123"}
|   GET       |   /api/v1/foods                | Get all food items menu    |
|   GET       |   /api/v1/foods/food_id        | Get a specific food item   | food_id required(int)
|  POST       |   /api/v1/foods                | Add a food item            | eg{"price": 450,"description": "Better than mom's food","title": "King of Burgers","creator": "fast-food-fast","type": "Snack","item_id": 0}
|  PUT        |   /api/v1/foods/food_id        | Edit food item data        | food_id required (int) eg {"price": 600,"description": "Better than mom's food","title": "King of Burgers","creator": "fast-food-fast","type": "Snack","item_id": 1}
| DELETE     |    /api/v1/foods/food_id        | Delete a food item         | food_id required (int)
|  GET        |  /api/v1/orders                | Get all Orders             | 
|  GET        |  /api/v1/orders/order_id       | Get a specific order       | order_id required(int)                     
|  DELETE     |  /api/v1/orders/order_id       | Delete order               | order_id required (int)
|  POST       |  /api/v1/orders                | Add an order               | e.g {"food_item": "Burger", "quantity": 20}     
|   PUT       |  /api/v1/orders/order_id       | Order status               |order_id required (int) eg{"status":"Declined"}
```` 

Run application on postman

  http://127.0.0.1:5000
  
#### Running test
on terminal run:
 pytest -vv
 then 
 nosetests  --with-coverage --cover-package=resources
 
 
 ***
 
 #### Built using

* python 3.5.2
* Flask
* flask-restplus

***

#### Heroku

https://fastfoodfastapi.herokuapp.com/

#### Versioning
Most recent version: version 1

***

#### Authors
Darius Ndubi

