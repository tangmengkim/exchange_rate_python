from bs4 import BeautifulSoup 
import requests
import json

def exchange_rate(URL,date = ""):
    data_list =[]
    res = requests.request('POST',URL)
    soup = BeautifulSoup(res.text,'html.parser')
    data_list= {
        'exchange_rate' : getCurrencyData(soup)
    }
    #convert dictionary to json_data
    json_data = json.dumps(data_list)
    return(json_data)

def getCurrencyData(soup):
    text = soup.find('table',class_='table')
    data_list ={}
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
        print("Unable to find data container (tbody) on the webpage.")

    return data_list