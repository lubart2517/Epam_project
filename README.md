# EPAM Online UA Winter 2021 final project - Library App


## With this app you can:
- ### Display a list of books and books authors, filter books by name, description, count and sort
  
- ### Display a list of authors
- ### Display a list of orders
- ### Display a list of users
- ### Change (add / edit / delete) the above data


## How to build this project:

- ### Navigate to the project root folder

- ### Optionally set up and activate the virtual environment:
```
virtualenv venv
source env/bin/activate
```

- ### Install the requirements:
```
pip install -r requirements.txt
```
- ### Configure Postgresql database

- ### Set the following environment variables:

```
export POSTGRES_USER=<your_postgresql_user>
export POSTGRES_PASSWORD=<your_postgresql_user_password>
export POSTGRES_SERVER=<your_postgresql_server>
export POSTGRES_DATABASE=<your_postgresql_database_name>
export POSTGRES_DATABASE_TEST=<your_postgresql_database_for_testing_name>
export API_KEY = <your_flask_api_key>
export FLASK_CONFIG=<class_of-config_to_use>
export FLASK_APP=app.py
export SECRET_KEY=<your_flask_secret_key>
```

*You can set these in .env file as the project uses dotenv module to load 
environment variables*

- ### Run migrations to create database infrastructure:
```
flask db upgrade
```

- ### Optionally populate the database with sample data from csv files
```
python -m library/sql/populate.py
```

- ### Run the project locally:
```
python -m flask run
```

## Now you should be able to access the web service and web application on the following addresses:

- ### Web Service:
```
localhost:5000/api/books
localhost:5000/api/books/<uuid>
localhost:5000/api/books/<name>
localhost:5000/api/books/<name>/<sort>

localhost:5000/api/author/<uuid>
localhost:5000/api/authors
```

- ### Web Application:
```
localhost:5000/
localhost:5000/register
localhost:5000/login
localhost:5000/logout

localhost:5000/admin/books
localhost:5000/admin/books/add
localhost:5000/admin/book/edit/id
localhost:5000/admin/book/delete/id

localhost:5000/admin/authors
localhost:5000/admin/authors/add
localhost:5000/admin/author/edit/id
localhost:5000/admin/author/delete/id

localhost:5000/admin/orders
localhost:5000/admin/order/close/id

localhost:5000/user/books
localhost:5000/user/authors
localhost:5000/user/orders
localhost:5000/user/book/order/id
```