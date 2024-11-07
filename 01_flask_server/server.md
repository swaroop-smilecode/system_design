Install the flask package.
```python
pip install Flask
```

Write code for server.
server.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hai, this is home page!"

app.run()
```

Start the server.
```python
python -m server
```
