import psycopg2
from config import database
    
config = psycopg2.connect(**database)
current = config.cursor()

create_table = '''
    create table snake(
        username VARCHAR(255),
        score INT
    );
''' 

current.execute(create_table)

current.close()
config.commit()
config.close()