import requests
import json 
from .util.Convereter_trunc import truncater

def getOraghData():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_Watch_Bonds',headers = head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        additionalDataMarketWatch(js)
        return js
    else:
        return ("noData")

def getHaghTaghadomData(): 
    resp = requests.get('http://37.152.180.99:3000/View_Watch_HaghTaghadoms')
    if resp.status_code == 200:
        js = json.loads(resp.text)
        additionalDataMarketWatch(js)
        return js
    else:
        return ("noData")


def additionalDataMarketWatch(data):
    for item in data:
        if item['yesterday'] !=None and item['close'] !=None:
            item['closePercent'] = truncater(((item['close']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['closePercent'] = None
        if item['last'] !=None and item['yesterday'] !=None:
            item['lastPercent'] = truncater(((item['last']-item['yesterday'])/item['yesterday'])*100)
        else:
            item['lastPercent'] = None