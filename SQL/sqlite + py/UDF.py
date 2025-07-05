import sqlite3
import pandas as pd

square = lambda n : n*n

with sqlite3.connect("BaseGrande.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute("Select *, square(Price) from Products where Price > 0")
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
    
print(results_df)