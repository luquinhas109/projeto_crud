import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("PASSWORD"),
        database="agrotech"
    )
    return conexao