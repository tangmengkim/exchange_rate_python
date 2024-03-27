from flask import Flask
from views import views_p
import os

PORT_SERVER = os.environ.get("PORT")
app = Flask(__name__)
app.register_blueprint(views_p)

if __name__ == '__main__':
    app.run(debug = True, port = PORT_SERVER)