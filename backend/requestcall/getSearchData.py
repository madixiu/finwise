import requests
import json

def SearchData():
    resp = requests.get('http://185.231.115.223:3000/View_SearchBar')
    resp2 = requests.get('http://45.147.77.195:3000/View_Search')
    if resp.status_code == 200 and resp2.status_code==200:
        return (json.loads('['+resp.text[1:-1]+', \n '+resp2.text[1:-1]+']'))
    else:
        return ("noData")