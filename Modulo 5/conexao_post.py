import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = 'Sony2006',
    host = 'localhost',
    port = '5432'
)