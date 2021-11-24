'''This script loads data from csv files to database without using sqlalchemy'''
import psycopg2
import csv
from dotenv import load_dotenv
import os

# loads environement variables with correct parameters for database connecting
load_dotenv()
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
database = os.environ.get('POSTGRES_DATABASE')

conn = psycopg2.connect(f"host=localhost dbname={database} user={user} password={password}")
cur = conn.cursor()
#  load Authors into db

with open('authors.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'Author', sep=';', null='')  # copy all records from csv file to database
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Author_id_seq" RESTART WITH {lines};')  # set next id value in the database
    conn.commit()


#  load Books into db
with open('books.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'Book', sep='&', null='')  # copy all records from csv file to database
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Book_id_seq" RESTART WITH {lines};')  # set correct next id value in the database
    conn.commit()

#  load info about book's authors into db
with open('Book_authors.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'book_authors', sep='&', null='')  # copy all records from csv file to database
    conn.commit()

#  load Users into db
with open('users.csv', 'r') as f:
    next(f)  # Skip the header row.
    cur.copy_from(f, 'users', sep=';', null='')
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "users_id_seq" RESTART WITH {lines};')  # set correct next id value in the database
    conn.commit()

#  load Orders into db
with open('orders.csv', 'r') as f:
    cur.copy_from(f, 'Order', sep=',', null='')
    f.seek(0)  # return to start of the file
    lines = len(list(csv.reader(f)))  # count number of records in the file
    cur.execute(f'ALTER SEQUENCE "Order_id_seq" RESTART WITH {lines};')  # set correct next id value in the database
    conn.commit()

conn.close()
