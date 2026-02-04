from lib.database_connection import *

connection = DatabaseConnection()
print(connection.connect())
print(connection.seed('seeds/social_network.sql'))