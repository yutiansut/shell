#import QUANTAXIS as QA

from core.CoreHandler import CoreHandler
import os

from core.CoreMongo import CoreMongo

from lib.Db import Db
import sys

class QaHandler(CoreHandler):

    def get(self): 
        
        db = Db()

        mongo = CoreMongo()
        indexDay = mongo.connection()
        rowNum = 0
        values = ""
        table_name = 'index_day'
        keys = ('close', 'up_count', 'code', 'amount', 'date', 'date_stamp', 'high', 'open', 'low', 'vol', 'down_count')
        key_str = "(";
        for key in keys:
            key_str += "`"+key+"`,"
        key_str = key_str.strip(",") + ")"
        #`open`, `close`, `high`, `low`, `amount`, `date`, `code`, `vol`) values "
        values = ""
        for doc in indexDay.find(): 
            values += "("
            if rowNum >= 999:
                rowNum = 0 
                for key in keys:
                    values += "'" + str(doc[key]) + "',"
                values = values.strip(",") + ")"

                db.connection("QUANTAXIS").table(table_name).insert(key_str, values)
                values = ""
            else:
                rowNum += 1
                for key in keys:
                    values += "'" + str(doc[key]) + "',"
                values = values.strip(',') + "),"

        values = values.strip(",")
        db.connection("QUANTAXIS").table(table_name).insert(key_str, values)
        self.write("over")

#            if rowNum >= 1000:
                    #ida.write(sql + values.strip(",") + ";\r")
                    #db.connection('QUANTAXIS').table("stock_day").insert("(`open`, `close`, `high`, `low`, `amount`, `date`, `code`, `vol`)", values.strip(","))
#                rowNum = 0
#                values = "" 
#            else:
#                rowNum += 1
#                values += "('" + str(doc["open"]) + "','" + str(doc['close'])+ "','" + str(doc['high'])+ "','" + str(doc['low'])+ "','" + str(doc['amount'])+ "','" + str(doc['date'])+ "','" + str(doc['code'])+ "', '" + str(doc['vol'])+ "'),"



