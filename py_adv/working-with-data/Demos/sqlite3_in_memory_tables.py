import sqlite3
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

create = '''CREATE TABLE beatles (
'fname' text,
'lname' text,
'nickname' text
)'''

cursor.execute(create)

members = [
    ('John', 'Lennon', 'The Smart One'),
    ('Paul', 'McCartney', 'The Cute One'),
    ('George', 'Harrison', 'The Funny One'),
    ('Ringo', 'Starr', 'The Quiet One')
]

for member in members:
    cursor.execute("INSERT INTO beatles VALUES" + str(member))

select = 'SELECT * FROM beatles'
cursor.execute(select)

results = cursor.fetchall()
cursor.close()
connection.close()

print(results)