import mysql.connector
from mysql.connector import errorcode

def connect_to_server(config):
    try:
        cnx = mysql.connector.connect(**config)
        print("Connected to MySQL server")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed to create database '{database_name}': {err}")

def check_and_create_database(config, database_name, tables):
    cnx = connect_to_server(config)
    if cnx is None:
        return None
    
    cursor = cnx.cursor()
    try:
        cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        result = cursor.fetchone()
        if result:
            print(f"Database '{database_name}' already exists.")
        else:
            create_database(cursor, database_name)
    except mysql.connector.Error as err:
        print(f"Error checking database '{database_name}': {err}")
        return None
    finally:
        cursor.close()
        check_and_create_tables(config, tables)
    
    
    cnx.close()
    return config

def create_table(cursor, table_name, table_description):
    try:
        print(f"Creating table '{table_name}'...")
        cursor.execute(table_description)
        print(f"Table '{table_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed to create table '{table_name}': {err}")

def check_and_create_tables(config, tables):
    cnx = connect_to_server(config)
    if cnx is None:
        return
    
    cursor = cnx.cursor()
    for table_name, table_description in tables.items():
        try:
            cursor.execute(f"DESCRIBE {table_name}")
            print(f"Table '{table_name}' already exists.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_TABLE_ERROR:
                create_table(cursor, table_name, table_description)
            else:
                print(f"Error checking table '{table_name}': {err}")

    cursor.close()
    cnx.close()

config={'host':'localhost', 'user':'root', 'password':'solo3111'}
database_name='data'
tables = {
        'registration':"CREATE table registration (name varchar(40) not null, dob date)",
        'log':"CREATE table log(user varchar(20) not null, time int)"}

check_and_create_database(config, database_name, tables)

