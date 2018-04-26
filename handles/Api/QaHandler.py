#import QUANTAXIS as QA

from core.CoreHandler import CoreHandler
import os

from core.CoreMongo import CoreMongo

from lib.Db import Db

class QaHandler(CoreHandler):

    def get(self): 
        
        db = Db()
        self.write("hh")

        mongo = CoreMongo()
        indexDay = mongo.connection()
        rowNum = 0
        values = ""
        sql = "insert into stock_day (`open`, `close`, `high`, `low`, `amount`, `date`, `code`, `vol`) values "
        with open("./indexDay2.txt", "w") as ida: 
            for doc in indexDay.find(): 
                if rowNum >= 1000:
                    #ida.write(sql + values.strip(",") + ";\r")
                    db.connection('QUANTAXIS').table("stock_day").insert("(`open`, `close`, `high`, `low`, `amount`, `date`, `code`, `vol`)", values.strip(","))
                    rowNum = 0
                    values = "" 
                else:
                    rowNum += 1
                    values += "('" + str(doc["open"]) + "','" + str(doc['close'])+ "','" + str(doc['high'])+ "','" + str(doc['low'])+ "','" + str(doc['amount'])+ "','" + str(doc['date'])+ "','" + str(doc['code'])+ "', '" + str(doc['vol'])+ "'),"







        


