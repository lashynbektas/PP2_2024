import psycopg2
# создаем таблицу телефонной книги
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='1234'
)

current = config.cursor()
sql = '''
        CREATE TABLE book(
            name VARCHAR(30),
            phone VARCHAR(30)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()