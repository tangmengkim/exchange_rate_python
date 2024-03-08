import os
import json
from flask import Flask
from utils import exchange_rate
app = Flask(__name__)

# get .env
ACLD_WEBSITE = os.environ.get("ACLD_WEBSITE")

@app.route('/')
def home():
    data = json.loads(exchange_rate(ACLD_WEBSITE))
   
    return data

if __name__ == '__main__':
    app.run(debug=True,port=8000)