import MySQLdb


class DB_Class:
    __host = "192.168.99.100"
    __user = "happy"
    __password = "happy"
    __port = 43306
    __db = "test"
    __cn = None
    __cur = None

    def __init__(self, host, user, password, port, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__db = db

        try:
            self.__cn = MySQLdb.connect(host=host, user=self.__user, passwd=self.__password, port=self.__port)
            self.__cn.select_db(self.__db)
            self.__cur = self.__cn.cursor()
        except MySQLdb.Error, e:
            print "init error %d: %s" % (e.args[0], e.args[1])

    def usedb(self, db):
        try:
            self.__db = db
            self.__cn.select_db(db)
            self.__cur = self.__cn.cursor()
        except MySQLdb.Error, e:
            print "usedb error %d: %s" % (e.args[0], e.args[1])

    def query(self, sql):
        if (self.__cur == None):
            print "No connection or cursor!"
        else:
            count = self.__cur.execute(sql)
            return count, self.__cur.fetchall()

    def queryOne(self, sql):
        if (self.__cur == None):
            print "No connection or cursor!"
        else:
            count = self.__cur.execute(sql)
            return self.__cur.fetchone()

class Data:
    db = None


def getDB():
    if Data.db == None:
        Data.db = DB_Class("192.168.99.100","happy","happy",43306,"ecom")
    return Data.db


#usage:
#import tools.MySQLdb_DB as DB
#db = DB.getDB()