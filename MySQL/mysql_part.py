from mysql.connector import connect, Error


# looks to local file to grab credentials to connect to SQL server, file should be formatted with each piece of info on a newline, in order as seen below
def database_credential_getter():
    with open(r"C:/Users/kimba/VSCode Projects/Room Temperature Project/room_temperature_database_credentials.txt", 'r') as f:
        database_credentials = [line.rstrip('\n') for line in f]
        HOST = database_credentials[0]
        USERNAME = database_credentials[1]
        PASSWORD = database_credentials[2]
        DATABASE = database_credentials[3]
        TABLE = database_credentials[4]
        return HOST, USERNAME, PASSWORD, DATABASE, TABLE


# creates the query and connects to the mysql database before inserting parameters as data into the table  
def data_entry_to_MySQL(parameters: dict):
    
    HOST, USERNAME, PASSWORD, DATABASE, TABLE = database_credential_getter()
    query = f"INSERT INTO {TABLE} ({', '.join(parameters)}) VALUES ({('%s, '*len(parameters)).rstrip(', ')})"
    args = [*parameters.values()]
    
    try:
        with connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE
        ) as connection:

            cursor = connection.cursor()
            cursor.execute(query, args)
            
            connection.commit()

    except Error as e:
        print(e)
