import sqlite3
connection = sqlite3.connect(':memory:')

create = '''CREATE TABLE states (
'state' text,
'pop2014' integer,
'pop2000' integer
)'''

insert = 'INSERT INTO states VALUES (?,?,?)'
        
select = '''SELECT state,
CAST( (pop2014*1.0/pop2000) * pop2014 AS INTEGER) pop2028
FROM states ORDER BY pop2028 DESC'''