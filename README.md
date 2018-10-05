[![Build Status](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API.svg?branch=ft-add-menu-item-160809873)](https://travis-ci.org/Darius-Ndubi/Fast-Food-Fast-API)  [![Coverage Status](https://coveralls.io/repos/github/Darius-Ndubi/Fast-Food-Fast-API/badge.svg?branch=ch-implement-feedback-160912719)](https://coveralls.io/github/Darius-Ndubi/Fast-Food-Fast-API?branch=ch-implement-feedback-160912719)
----

# Fast-Food-Fast-API
- Fast-Food-Fast is a food delivery service app for a restaurant. The restraunt provides a service to its contomers.
Customers are allowed to view all food items and if they choose to create an  order they should signup and be authorized users. After authorization the user can now actually create orders of there choice . The user has the freedom to choose the number of items to order so long as they are in the menu. After creating an order the user awaiting for admins aproval and procedures. An order is considered as an item in diffrent states. If the last order the user created is still new, The user can add more orders to it. But if the status changes to processng then the user creates a new order.

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
Create a virtual enviroment. *virtualenv name_of_virtual_enviroment.
Folder with the 'name_of_virtual_enviroment' will be created and that is out enviroment.
Navigate inside the folder, open folder called Scripts or scripts and run the script activate. *Type activate
Clone this repo to your local computer using git clone https://github.com/Darius-Ndubi/Fast-Food-Fast-API
Switch into the project directory
Install the project's dependencies by running pip install -r requirements.txt
Run the app locally with python run.py or python3 run.py
Navigate to your project folder and open it using the terminal.

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

  http://127.0.0.1:5000/api.v2/auth/signup 
  

  
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
https://dariusndubi.docs.apiary.io/#introduction/authentication

*********

#### Versioning
Most recent version: version 2

***

#### Authors
Darius Ndubi
 
 
  
 
