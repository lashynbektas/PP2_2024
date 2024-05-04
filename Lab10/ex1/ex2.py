# 2 Implement two ways of inserting data into the PhoneBook

# 2.1 upload data from csv file
import psycopg2

conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='1234',
	host='localhost'
)
cursor = conn.cursor()
conn.autocommit = True
# CSV to TABLE

f = open("persons.csv", "r")
cursor.copy_from(f, 'phonebook', sep=',')
f.close()


# 2.2 insert entering user name, phone from console

first = str(input("First: "))
last = str(input("Last: "))
num = int(input("Num: "))


postgres_insert_query = """ INSERT INTO  phonebook(first_name, last_name, phone_num) VALUES (%s,%s,%s)"""
record_to_insert = (first, last, num)
cursor.execute(postgres_insert_query, record_to_insert)


conn.commit()
print("successfully !!");
conn.close()