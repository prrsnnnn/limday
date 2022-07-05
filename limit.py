import time
from pymongo import MongoClient
mongo_token="mongodb+srv://prrsnnnn:300505waffy@clusterbot.xxs0g.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(mongo_token, port=27017)
telebot = mongo["Telegrambot"]
settings=telebot['Settings']
while True:
    if time.localtime().tm_hour ==20  and time.localtime().tm_min == 20 and time.localtime().tm_sec == 15:
        #print(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
        for l in settings.find({}, {'out': 1}):
            settings.update_one({'out': l['out']}, {"$set": {'day': 0}})
            print(1)
            break
        time.sleep(1)