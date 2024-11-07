from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hai, this is home page!"

app.run()