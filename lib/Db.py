
"""
公共DB类库
"""
import MySQLdb
import sys
import configparser
import logging
import MySQLdb.cursors

class Db (object): 

    tablename = None
    connect = None
    cur = None
    fields = ""

    """ 
    初始化数据库配置
    """
    def __init__(self): 
        self._where = ""
        self.logger = logging.getLogger(__name__)

    """
    切换数据库连接
    """
    def connection(self, param = ""):
        configParser = configparser.ConfigParser()
        configParser.read("configs/config.ini")
        
        dbConfig = configParser[param]
        self.connect = MySQLdb.connect(
                host = dbConfig['host'],
                user = dbConfig['user'],
                passwd = dbConfig['passwd'],
                db = dbConfig['db'],
                port = int(dbConfig['port']),
                charset = dbConfig['charset'],
                cursorclass = MySQLdb.cursors.DictCursor
                )
        self.cur = self.connect.cursor()
        return self

    """
    设置查询表
    """
    def table(self, tablename):
        self.tablename = tablename
        return self

    """
    查询条件
    """
    def where(self, key, value, oprate = "="):
        self._where = self._where + "and `" + key + "` " + oprate +  " '"+ str(value)+"' "
        return self
    
        
    """
    执行原生SQL
    """
    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    """
    组合SQL
    """
    def combinationSql(self):
        if self._where:
            self._where = self._where.strip("and ")

        if self.fields == "": 
            self.fields = "*"

        self._sql = "SELECT " + self.fields + " FROM " + str(self.tablename) + " WHERE " + self._where
        return self

    """
    设置查询字段
    """
    def field(self, fieldname):
        self.fields = self.fields + "," + filedname
        self.fields = self.fields.strip(",")
        return self


    """
    只获取一条数据 xxx
    """
    def first(self):
        if self.tablename == None or self.tablename == '':
            return False 

        self.combinationSql()
        print(self._sql)
        self.cur.execute(self._sql)
        return self.cur.fetchone()
    """
    根据条件获取查询所有数据
    """
    def get(self):
        if self.tablename == None:
            return False
        _where = ""

        if self._where:
            _where += " where " + self._where.strip("and ")
        dsql = "select * from " + str(self.tablename) + " " + _where
        self.cur.execute(dsql)
        return self.cur.fetchall()


    """
    新增数据
    """
    def insert(self, keys = '', values = ''):
        if self.tablename == None:
            return False
        if len(values) <= 0 or len(keys) <= 0:
            return False

        dsql = "INSERT INTO `" + self.tablename + "` "+keys+" values " + values + ";"
        result = self.cur.execute(dsql)
        self.cur.close()
        self.connect.commit()
        self.connect.close()
        return result


    """
    新增数据，返回操作的ID
    """
    def insertGetId(self, sql, value=""):
        if self.cur == None :
            self.connection("TEST")
        if value != '':
            self.cur.execute(sql, value)
        else :
            self.cur.execute(sql)
        self.connect.commit()
        rowCount = self.cur.rowcount()
        self.connect.close()
        return rowCount

    """
    更新数据
    """
    def update(self,data):
        updateData = "" 
        param = ()
        for key in data:
            updateData += " `" + key + "`=%s,"
            param.append(data[key])
        #updateData = updateData.strip(",")

        where = ""
        if self._where != None:
            where = " where " + self._where

        sql = "update " + self.tablename + " set " + updateData + where;

        result = self.cur.execute(sql)
        self.connect.commit()
        self.connect.close()
        return result
    """
    插入多条 cur.executemany
    """



        



