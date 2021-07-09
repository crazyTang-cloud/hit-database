import pymysql
import sys

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="tian668",
#     database="tourism")
#
# cursor = db.cursor()

def delete(db,cursor,name,condition,value):
# def delete(name,condition,value):

    db.ping(True)
    sql='delete from {name} where {condition}={value}'\
        .format(name=name,condition=condition,value=value)
    print(sql)
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


# delete("routes","route_id",3)