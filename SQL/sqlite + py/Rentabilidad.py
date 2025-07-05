import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('BaseGrande.db')
# query= '''
#     select ProductName, sum(Price * Quantity) as Revenue
#     from OrderDetails od
#     join products p on p.ProductID = od.ProductID 
#     group by od.ProductID
#     order by Revenue desc
#     limit 10
# '''
# top_products = pd.read_sql_query(query, conn)
# top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10,5),
# legend=False
# )
# plt.title("10 Productos más vendidos")
# plt.xlabel("Productos")
# plt.ylabel("Revenue")
# plt.xticks(rotation=90)
# plt.show()



query2= '''
    select FirstName || " " || LastName as Employee, count(*) as Total
    from orders o 
    join Employees e
    on o.EmployeeID = e.EmployeeID
    group by o.EmployeeID
    order by Total asc
    limit 3
'''
top_employees = pd.read_sql_query(query2, conn)
top_employees.plot(x="Employee", y="Total", kind="bar", figsize=(10,5),
legend=False
)
plt.title("10 Productos más efectivos")
plt.xlabel("Empleado")
plt.ylabel("Total vendido")
plt.xticks(rotation=45)
plt.show()
