#### Install the flask package.
```python
pip install Flask
```

#### Write code for server.
server.py
```python
from flask import Flask

app = Flask(__name__)

def prices():
    plant_prices = {
                    "rose" : 100,
                    "orchid" : 200,
                    "marigold" : 300
                }
    data = ""
    for plant, price in plant_prices.items():
        data += f"{plant} : {price} <br/>"
    return data

@app.route('/')
def home():
    return prices()

app.run()
```

#### Start the server.
```python
python -m server
```
OR
```python
flask --app server run
```

#### Send a request from browser to server
`http://127.0.0.1:5000`</br>
You will see the below response.</br>
rose : 100 </br>
orchid : 200 </br>
marigold : 300
