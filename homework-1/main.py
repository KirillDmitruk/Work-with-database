import pandas as pd
import psycopg2
from config import customers_file, employees_file, orders_file

customers = pd.read_csv(customers_file)
employees = pd.read_csv(employees_file)
orders = pd.read_csv(orders_file)

with psycopg2.connect(host="localhost", database="north", user="postgres", password="13Keb-09") as conn:
    with conn.cursor() as cursor:
        for customer in customers.itertuples(index=False):
            cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)", customer)

        for employee in employees.itertuples(index=False):
            cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employee)

        for order in orders.itertuples(index=False):
            cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", order)

conn.close()