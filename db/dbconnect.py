import pymysql
from configs import dbConfig

def dbConnect():
    dbHandle = None

    try:
        dbHandle = pymysql.connect(host=dbConfig.dbHostname,user=dbConfig.dbUsername,password=dbConfig.dbPassword,database=dbConfig.dbDatabase,cursorclass=pymysql.cursors.DictCursor)

        print('MySQL: Connected')

    except Exception as ex:
        print('MySQL: Connection failed')
        print(ex)

    return dbHandle