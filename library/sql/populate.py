import psycopg2
conn = psycopg2.connect("host=localhost dbname=Epam user=postgres password=postgres")
cur = conn.cursor()

with open('authors.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'Author', sep=';', null='')
conn.commit()

with open('books.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'Book', sep='&', null='')
conn.commit()

with open('Book_authors.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'book_authors', sep='&', null='')
conn.commit()

with open('users.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=';', null='')
conn.commit()

with open('orders.csv', 'r') as f:
    cur.copy_from(f, 'Order', sep=',', null='')
conn.commit()