#!/usr/bin/python3
import os

from mysql.connector import connect

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'toorroot',
    'allow_local_infile': True,
}


# Establish MySql connection
def connect_db():
    """ connects to the mysql database server """
    try:
        connection = connect(**db_config)
        return connection
    except Exception as e:
        print(e)


# Create Database ALX_prodev
def create_database(connection):
    """ creates the database ALX_prodev if it does not exist """
    query = 'CREATE DATABASE IF NOT EXISTS ALX_prodev'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()


# Select ALX_prodev database
def connect_to_prodev():
    """ connects the ALX_prodev database in MYSQL """
    try:
        connection = connect(database='ALX_prodev', **db_config)
        return connection
    except Exception as e:
        print(e)


# Create table - user_data
def create_table(connection):
    """ creates a table user_data if it does not exists with the required fields """
    query = (f'CREATE TABLE IF NOT EXISTS user_data ('
             f'user_id VARCHAR(36) NOT NULL PRIMARY KEY DEFAULT (UUID()),'
             f'name VARCHAR(255) NOT NULL,'
             f'email VARCHAR(255) NOT NULL,'
             f'age DECIMAL NOT NULL,'
             f'INDEX(user_id))'
    )

    cursor = connection.cursor()

    cursor.execute(query)


def insert_data(connection, data):
    """ inserts data in the database if it does not exist """
    cursor = connection.cursor()
    query = f"""
    LOAD DATA LOCAL INFILE '{data}'
        INTO TABLE user_data
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\\n'
        IGNORE 1 LINES
        (name,email,age)
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
