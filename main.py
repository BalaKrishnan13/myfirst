import psycopg2

conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="123456")
cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('CREATE TABLE user3 (id INT, name VARCHAR(255))')
conn.commit()

print("Finished!")
