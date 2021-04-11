import requests
import json
#define a class to get data from web
class AnimalUtil():
    def __init__(self, name,type1):
        self.name = name
        self.type = type1
#searching animals by using name data
    def GetAnimalFromAPI(self): 
        url = "http://api.tianapi.com/txapi/pet/index?key=3400d776e33b9e3ecfb1a8822aa4f0ee&name=" + self.name
        r = requests.get(url)
        data_str =  r.content.decode("utf-8")
        data_dict = json.loads(data_str)
        if data_dict["code"] != 200:
            return {}
        else:
            return data_dict
#searching animals of the certain type by using api     
    def GetTypeFromAPI(self): 
        url = "http://api.tianapi.com/txapi/pet/index?key=3400d776e33b9e3ecfb1a8822aa4f0ee&page=1&num=15&type=" + self.type
        r = requests.get(url)
        data_str =  r.content.decode("utf-8")
        data_dict = json.loads(data_str)
        url = "http://api.tianapi.com/txapi/pet/index?key=3400d776e33b9e3ecfb1a8822aa4f0ee&page=2&num=15&type=" + self.type
        r1 = requests.get(url)
        data_str1 =  r1.content.decode("utf-8")
        data_dict1 = json.loads(data_str)
        data_dict['newslist']=data_dict['newslist']+data_dict1['newslist']
        if data_dict["code"] != 200:
            return {}
        else:
            return data_dict