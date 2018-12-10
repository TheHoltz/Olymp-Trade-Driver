import requests
from lxml import html
import pandas as pd
import numpy as np

def getdata():
    try:
        resp = requests.get(url='https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=demo')
        out = resp.json()
        with open("out.txt","w") as f:
            f.write(str(out))
        print("[200] Dados extraídos com sucesso.")
    except:
        print("[401] Houve um erro durante a extração.")

def importData():
    In = open("out.txt","r")
    out = eval(In.readlines()[0])
    return(out)

def convertData(obj):
    out = list()
    outConverted = list()
    for data in obj['Time Series FX (5min)']:
        for tempo in obj['Time Series FX (5min)'][data]:
            out.append(str(obj['Time Series FX (5min)'][data][tempo]))
    for i in range(0, len(out), 4):
        outConverted.append(out[i:i+4])
    return(outConverted)

getdata()
dados = convertData(importData())
dados = pd.DataFrame(np.array(dados), columns = ['open','high','low','close'])

print(dados)
