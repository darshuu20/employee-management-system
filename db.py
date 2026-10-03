import os
import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="employee_management"
    )

    return connection