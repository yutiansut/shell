
import pymongo as pm
import sys

class CoreMongo(object):

    def __init__(self):
        pass
        #self.connection()

    def connection(self, config = ''):
        # 数据库连接
        client = pm.MongoClient('localhost', 27017)
        # 连接数据库
        db = client.quantaxis
        # 获取集合
        indexDay = db.stock_day
        return indexDay 
#        rowNum = 0
#        values = ""
#        sql = "insert into (`open`, `close`, `high`, `low`, `amount`, `date`, `code`) values "
#        with open("./indexDay.txt", "w") as ida: 
#            for doc in indexDay.find(): 
#                if rowNum >= 1000:
#                    ida.write(sql + values.strip(",") + "\r\n")
#                    rowNum = 0
#                    values = ""
#                else:
#                    rowNum += 1
#                    values += "('" + str(doc["open"]) + "','" + str(doc['close'])+ "','" + str(doc['high'])+ "','" + str(doc['low'])+ "','" + str(doc['amount'])+ "','" + str(doc['date'])+ "','" + str(doc['code'])+ "'),"
#
#
#
#
#
#
#mongo = CoreMongo()
