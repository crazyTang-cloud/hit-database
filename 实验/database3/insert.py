import pymysql
import sys

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="tian668",
#     database="tourism")
#
# cursor = db.cursor()
def insert(db,cursor,name,*value):
# def insert(name,*value):
    db.ping(True)
    sql = 'insert into {name} values {value}'.format(name=name,value=value)
    print(sql)
    # sql = 'insert into routes values(1,"哈尔滨","上海",10,"东方明珠")'
    try:
        execute = cursor.execute(sql)
        db.commit()
    except:
        info = sys.exc_info()
        print("error")
        print(info[0], ":", info[1])
        db.rollback()
    finally:
        db.close()


# insert("accompany",1,2)