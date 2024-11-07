from flask import Flask
from setup_database import setup_database
from db_queries import read_database

setup_database()
app = Flask(__name__)

def process_data(db_rows):
    response = ""
    for id, name, price in db_rows:
        response += f"{name} : {price} </br>"
    print(response)
    return response

@app.route('/')
def home():
    db_rows = read_database()
    response = process_data(db_rows)
    return response

app.run()