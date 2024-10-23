import requests
import pandas as pd
from keys import GetKeys
import time

df = pd.read_excel("./data/S&P500_stocks.xlsx")

symbols = df['Symbol']
res = pd.DataFrame()


y = 0

for x in symbols:
    url = f'https://api.polygon.io/v2/aggs/ticker/{x}/range/2/week/2022-10-01/2024-10-21?adjusted=true&sort=desc&apiKey=o4GUN1bkIRJWjhmzUibnbo7RekNvspAs'
    r = requests.get(url)
    data = r.json()
    temp = pd.DataFrame(data['results'])
    temp['Symbol'] = x
    if(x == 'APPL'):
        res = temp
        res.to_csv("./data/StockData.csv", index = False)
    else:
        temp.to_csv("./data/StockData.csv", index = False, header = False, mode = 'a')
        try:
            res = pd.concat([res, temp], ignore_index=True)
        except Exception as e:
            print("ran out of requests")

    
    y += 1
    print(f'sleeping for {x} iter {y}')
    time.sleep(15)

    

print(res.shape)
print("Writing to CSV file")
res.to_csv("./data/Stock_Data_Final.csv", index = False)






#__________________________________________________________________________________________________________________
#keys = GetKeys()
# keys[0]

# url = f'https://api.polygon.io/v2/aggs/ticker/{symbols[0]}/range/2/week/2022-10-01/2024-10-21?adjusted=true&sort=desc&apiKey=o4GUN1bkIRJWjhmzUibnbo7RekNvspAs'


# #url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={symbols[0]}&apikey={keys[0]}'
# r = requests.get(url)
# data = r.json()

# df = pd.DataFrame(data['results'])

# df['Symbols'] = 'APPL'
