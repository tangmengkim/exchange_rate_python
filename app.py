import os
import json
from flask import Flask
from utils import exchange_rate
app = Flask(__name__)

<<<<<<< HEAD
# get .env
=======
#  .env
>>>>>>> mengkim
ACLD_WEBSITE = os.environ.get("ACLD_WEBSITE")

@app.route('/')
def home():
    data = json.loads(exchange_rate(ACLD_WEBSITE))
<<<<<<< HEAD
    print(data[0]['USD']['bid'])
    return data


=======
   
    return data

>>>>>>> mengkim
if __name__ == '__main__':
    app.run(debug=True,port=8000)