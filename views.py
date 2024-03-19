from flask import Blueprint, render_template, request
from utils import exchange_rates
import json

views_p = Blueprint(__name__,'views')

@views_p.route('/', methods=['GET'])
def index():
    exchange_rate = json.loads(exchange_rates())
    if exchange_rate['status_code'] == 200:
        return render_template('test.html', data=exchange_rate)
    else:
        return ('no internet connection')

@views_p.route('/edit', methods = ['POST'])
def process_data():
    if request.method == 'POST':
        # Access form data
        date_status = request.form.get('date_input')

        # Process the data and load data as JSON
        exchange_rate = json.loads(exchange_rates( date_status ))
        if exchange_rate['status_code'] == 200:

            return render_template('test.html',data=exchange_rate)
        else:
            return ('no internet connection')

@views_p.route('/test', methods=["GET"])
def testing():
    return render_template("test.html")