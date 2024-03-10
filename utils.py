from bs4 import BeautifulSoup 
from datetime import datetime
import requests
import json
import os


def exchange_rates(date=''):
    response = request_URL(date)
    if response != None:
        currencyData = getCurrencyData(response)
        date = getDateOfData(response)

        data_list= {
            'status_date': date ,
            'exchange_rate' : currencyData ,
            'status_code' : 200
        }
    else:
        data_list={
            'status_date':'',
            'exchange_rate':'',
            'status_code' : 404
        }
    #convert dictionary to json_data
    json_data = json.dumps(data_list)
    return(json_data)


def request_URL(date):
    # get .env
    ACLD_WEBSITE = os.environ.get("ACLD_WEBSITE")

    payload = ''
    headersList = {
        "Content-Type": "application/x-www-form-urlencoded" 
        }
    
    if date:
        payload = f"edit1={date}"
    try:
        res = requests.request('POST',ACLD_WEBSITE,data=payload,headers=headersList) 
    # Check connection_status

        res.raise_for_status()  # Raise an error for bad responses (4xx or 5xx status codes)

        soup = BeautifulSoup(res.text,'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Request failed. Error: {e}")
        return None
    

def getDateOfData(soup):
    date_string = soup.find('div').text.strip()
    # Try to convert with time
    try:
        date_object = datetime.strptime(date_string, "%B %d, %Y %I:%M %p")
    # If parsing with time fails, try without time
    except ValueError:
        date_object = datetime.strptime(date_string, "%B %d, %Y")

    # Format as "YYYY-MM-DD"
    date = date_object.strftime("%Y-%m-%d")
    return date


def getCurrencyData(soup):
    data_list ={}
    # Seleted location of data
    text = soup.find('table',class_='table')
    if text:
    # Iterate through rows and print exchange rates
        for row in text.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) >= 2:
                currency = columns[0].text.strip()
                toCurrency,bid = columns[1].text.strip().split()
                toCurrency,ask = columns[2].text.strip().split()
                if toCurrency == 'KHR':
                    data_currency ={
                        currency : {
                            'ask' : ask.replace(',',''),
                            'bid' : bid.replace(',','')
                        }
                    }
                    data_list.update(data_currency)
    else:
        data_list = None
    return data_list



