import sqlite3
connection = sqlite3.connect('../lahman2016.sqlite')

query = '''SELECT nameFirst, nameLast, weight, strftime('%Y', debut / 1000, 'unixepoch')
FROM Master
ORDER BY weight DESC
LIMIT 5'''

# YOUR CODE HERE