import requests
import json
from .util.Convereter_trunc import truncater
def getMapData():
    res = requests.get("http://37.152.180.99:3000/View_TreeMapInitial")


    js = json.loads(res.text)
    temp = js[0]["industry"]
    TempMarketCap = 0
    final = []
    child = []
    industryList =[]

    for item in js:
        if not item["industry"] in industryList:
            industryList.append(item["industry"])
    for item in js:
        if (item["industry"] == temp):
            TempMarketCap+=item["MarketCap"]
            child.append({"name": item["ticker"],"scale": item["MarketCap"]})
            if item["industry"] == industryList[-1] and item == js[-1]:
                final.append({"name": temp, "children": child ,"scale": TempMarketCap})

        elif item["industry"] != temp and item["industry"] != industryList[-1]:
            final.append({"name": temp, "children": child ,"scale": TempMarketCap})
            TempMarketCap = item["MarketCap"]
            temp = item["industry"]
            child=[]
            child.append({"name": item["ticker"],"scale": item["MarketCap"]})
        elif item["industry"] != temp and item["industry"] == industryList[-1]:
            final.append({"name": temp, "children": child ,"scale": TempMarketCap})
            TempMarketCap = item["MarketCap"]
            temp = item["industry"]
            child=[]
            child.append({"name": item["ticker"],"scale": item["MarketCap"]})

    # print(final)
    mapDataObj = {"children":[{"name": "بورس ایران", "children":final}]}
    # print(mapDataObj)

    prices={}
    k={}
    for item in js:
        j={}
        j['p']=item['p']
        # print(item['cp'])
        if item['cp'] != None:
            j['cp']=truncater(item['cp'])
        k[item['ticker']]=j
    prices['errCode']=0
    prices['msg']=''
    prices['data']=k


    # return json.dumps({"mapDataObj":mapDataObj,"prices":prices
    # })
    # return json.dumps([mapDataObj,prices])
    result = {"mapDataObj":mapDataObj,"prices":prices}
    # print(mapDataObj)
    return result
    # }
    # print("####################################")
    # print(prices)
# getMapData()
# print(len(mapDataObj["children"][0]["children"]))
# print(len(industryList))
