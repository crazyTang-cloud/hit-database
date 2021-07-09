import pymysql
import sys

db = pymysql.connect(
    host="localhost",
    user="root",
    password="tian668",
    database="tourism")

cursor = db.cursor()
sql=''

def join_query(db,cursor,num,condition):
# def join_query(num,condition):
    db.ping(True)
    if num=="1":
#  根据旅游班次查导游信息
        sql='select g.name,g.sex,g.phone_num,g.language,' \
            'g.level,g.achievement from guide g,accompany a where' \
            ' a.frequency_id={condition} and g.guide_id=a.guide_id'.format(condition=condition)
    elif num=="2":
#  根据旅游班次查宾馆信息
        sql='select h.name,h.city,h.star_level,h.cost,h.contact,h.phone_num' \
            ' from hotel h,board b where ' \
            'b.frequency_id={condition} and b.hotel_id=h.hotel_id'.format(condition=condition)
    elif num=="3":
#  根据班次查路线
        sql='select r.origin,r.destination,r.days,r.main_attractions' \
            ' from routes r,frequency f where f.frequency_id={condition} ' \
            'and f.route_id=r.route_id'.format(condition=condition)
    elif num=="4":
#   根据旅游班次查出发交通信息（包括出发日期）
        sql='select t.start_tool,f.start_date,t.start_time,t.start_num ' \
            'from frequency f,traffic t ' \
            'where f.frequency_id={condition} and f.frequency_id=t.frequency_id'.format(condition=condition)
    elif num=="5":
#   根据旅游班次查回程交通信息（包括回程日期）
        sql='select t.end_tool,f.end_date,t.end_time,t.end_num ' \
            'from frequency f,traffic t ' \
            'where f.frequency_id={condition} and f.frequency_id=t.frequency_id'.format(condition=condition)
    elif num=="6":
#    根据团名查保险
        sql='select i.insurance_id,i.cost,i.date ' \
            'from tourist_group tg,insurance i ' \
            'where tg.group_name=\"{condition}\" and tg.group_id=i.group_id'.format(condition=condition)
    else:
        sql=''

    execute = cursor.execute(sql)
    fetchall = cursor.fetchall()

    for i in fetchall:
        print(i)

def nest_query(db,cursor,num,condition):
# def nest_query(num,condition):
    db.ping(True)
    if num == "1":
        #  根据旅游班次查导游信息
        sql = 'select g.name,g.sex,g.phone_num,g.language,g.level,g.achievement ' \
              'from guide g where ' \
              'g.guide_id in (' \
              'select guide_id from accompany ' \
              'where frequency_id={condition})'.format(condition=condition)
    elif num == "2":
        #  根据旅游班次查宾馆信息
        sql = 'select h.name,h.city,h.star_level,h.cost,h.contact,h.phone_num' \
              ' from hotel h where ' \
              'h.hotel_id in (' \
              'select hotel_id from board ' \
              'where frequency_id={condition})'.format(condition=condition)
    elif num == "3":
        #  根据班次查路线
        sql = 'select r.origin,r.destination,r.days,r.main_attractions' \
              ' from routes r where ' \
              'r.route_id in (' \
              'select route_id from frequency ' \
              'where frequency_id={condition})'.format(condition=condition)
    elif num == "4":
        #    根据团名查保险
        sql = 'select i.insurance_id,i.cost,i.date ' \
              'from insurance i ' \
              'where i.group_id in (' \
              'select group_id from tourist_group ' \
              'where group_name=\"{condition}\")'.format(condition=condition)
    else:
        sql = ''

    execute = cursor.execute(sql)
    fetchall = cursor.fetchall()

    for i in fetchall:
        print(i)


def group_query(db,cursor,num,condition):
# def group_query(num):
    db.ping(True)
    if num=="1":
        sql='select count(*) ,sex from guide ' \
            'group by sex having sex=\"{condition}\"'.format(condition=condition)
    elif num=="2":
        sql='select count(*),star_level ' \
            'from hotel group by star_level having ' \
            'star_level={condition}'.format(condition=condition)
    else:
        sql=''

    execute = cursor.execute(sql)
    fetchall = cursor.fetchall()

    for i in fetchall:
        print(i)


def view_query(db,cursor,num,condition):
# def view_query(num,condition):
    db.ping(True)
    if num=="1":
        sql='select * from view_guide where ' \
            'guide_id={condition}'.format(condition=condition)
    elif num=="2":
        sql='select * from view_tourist where ' \
            'tourist_name={condition}'.format(condition=condition)
        print(sql)
    elif num=="3":
        sql='select * from view_tourist where ' \
            'tourist_id={condition}'.format(condition=condition)
        print(sql)

    execute = cursor.execute(sql)
    fetchall = cursor.fetchall()

    for i in fetchall:
        print(i)


