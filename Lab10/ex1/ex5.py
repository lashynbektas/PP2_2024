# 5 Implement deleting data from tables by username of phone
import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='1234',
	host='localhost'
)
cursor = conn.cursor()
conn.autocommit = True


#looking with the first and last name
first_old = str(input("First_old: "))
last_old = str(input("Last_old: "))

sql = f"select * from phonebook where first_name =\'{first_old}\' and last_name = \'{last_old}\' "
cursor.execute(sql)
info = cursor.fetchall()


if len(info) > 0:
    sql_update = f"Delete from phonebook where  first_name =\'{first_old}\' and last_name = \'{last_old}\'; " 
    cursor.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()