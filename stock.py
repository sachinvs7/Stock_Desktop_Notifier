#Import libraries
import urllib2
from bs4 import BeautifulSoup
quote_page = 'https://www.moneycontrol.com/stocksmarketsindia/'
#Query the website and return the html to the variable "page"
page = urllib2.urlopen(quote_page)

def fetch_stock_details():

    data = []
    final = []
    
    soup = BeautifulSoup(page, 'html.parser')
    #Sensex
    index_1 = soup.find('a', attrs={'class': 'acord_title'})
    index_1 = index_1.text.strip()
    #Nifty 50
    index_2 = soup.find('a', attrs={'class': 'acord_title collapsed'})
    index_2 = index_2.text.strip()
    #Top gaining stock of the day
    top_gain = soup.find('a', attrs={'title': 'equity'})
    top_gain = top_gain.text.strip()
    
    data.extend((index_1,index_2))
      
    
    for value in soup.find_all('div', attrs={'class': 'disin'}, limit = 2):
        data.append(value.text)
    
    sensex = data[::2]
    nifty = data[1:][::2]
    
    final = sensex + nifty
    final.append((top_gain))

    #print(final)
    return final

final = fetch_stock_details()
#Desktop notification using notify-send
text = ""
for i in final:
    text = text + i + "\r"

import subprocess as s
 
s.call(["notify-send", text])
