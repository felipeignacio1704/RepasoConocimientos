import mysql.connector

config ={
    "host" : "127.0.0.1",
    "port" : "3306",
    "database" : "Test2025",
    "user" : "root",
    "password" : "",
}

conection = mysql.connector.connect(**config)
cursor = conection.cursor()

query = "select * from persona"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)
    
cursor.close()
conection.close()