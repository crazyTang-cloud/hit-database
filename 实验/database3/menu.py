from array import array

import pymysql
import insert
import delete
import query
import os				# 导入os模块
import sys

db = pymysql.connect(
    host="localhost",
    user="root",
    password="tian668",
    database="tourism")

cursor = db.cursor()
# insert.insert(db,cursor,"accompany",1,2)


def describe_table():
    print("旅游管理信息系统关系表如下：")
    print("1、routes(route_id,origin,destination,day,main_attractions)")
    print("2、frequency(frequency_id,route_id,start_date,end_date,cost)")
    print("3、tourist_group(group_id,frequency_id,group_name,people_num,contact,address,phone_num)")
    print("4、tourist(tourist_id,group_id,name,sex,age,identity_num,address,phone_num)")
    print("5、guide(guide_id,name,sex,age,identity_num,address,phone_num,language,level)")
    print("6、traffic(frequency_id,start_tool,start_time,start_num,end_tool,end_time,end_num)")
    print("7、hotel(hotel_id,name,city,star_level,cost,contact,job,address,phone_num)")
    print("8、insurance(insurance_id,group_id,people_num,cost,date)")
    print("9、accompany(frequency_id,guide_id)")
    print("10、board(frequency_id,hotel_id)")

def num_to_tablename(num):
    if num=="1":
        return "routes"
    elif num=="2":
        return "frequency"
    elif num=="3":
        return"tourist_group"
    elif num=="4":
        return "tourist"
    elif num=="5":
        return "guide"
    elif num=="6":
        return "traffic"
    elif num=="7":
        return "hotel"
    elif num=="8":
        return "insurance"
    elif num=="9":
        return "accompany"
    elif num=="10":
        return "board"
    else:
        return -1;

def describe_view():
    print("旅游管理信息系统视图表如下：")
    print("1、view_guide(guide_id,name,phone_num)")
    print("2、view_tourist(tourist_id,tourist_name,group_id,guide_name,guide_phone)")


def menu():
    os.system("cls")  # 执行cls命令清空Python控制台
    print()
    describe_table()
    describe_view()
    print()
    print("请输入序号选择操作")
    print("1、插入")
    print("2、删除")
    print("3、连接查询")
    print("4、嵌套查询")
    print("5、分组查询")
    print("6、视图查询")
    print("7、事务管理")
    print("输入其它键退出")
    num=input()
    if num=="1":
        menu_insert()
    elif num=="2":
        menu_delete()
    elif num=="3":
        menu_join_query()
    elif num=="4":
        menu_nest_query()
    elif num=="5":
        menu_group_query()
    elif num=="6":
        menu_view_query()
    elif num=="7":
        menu_transaction()
    else:
        return

def menu_insert():
    os.system("cls")  # 执行cls命令清空Python控制台
    print()
    describe_table()
    print()
    num=input("请选择关系表：")
    if num=='':
        menu()
    table_name=num_to_tablename(num)
    s = input("请输入要插入的数据(用逗号分割)")
    split = s.split(",")
    tuple(split)
    insert.insert(db,cursor,table_name,*tuple(split))
    input1 = input("输入1继续插入，否则退出")
    if input1=="1":
        menu_insert()
    else:
        menu()


def menu_delete():
    describe_table()
    num = input("请选择关系表：")
    if num == '':
        menu()
    table_name = num_to_tablename(num)
    s = input("请输入要删除的条件(等值查询)")
    split = s.split("=")
    delete.delete(db,cursor,table_name,split[0],split[1])
    input1 = input("输入1继续删除，否则退出")
    if input1 == "1":
        menu_delete()
    else:
        menu()

def menu_join_query():
    print("1、根据旅游班次查导游信息")
    print("2、根据旅游班次查宾馆信息")
    print("3、根据班次查路线")
    print("4、根据旅游班次查出发交通信息（包括出发日期）")
    print("5、根据旅游班次查回程交通信息（包括回程日期）")
    print("6、根据团名查保险")
    s = input("请输入编号")
    s1 = input("请输入条件")
    query.join_query(db,cursor,s,s1)
    input1 = input("输入1继续查询，否则退出")
    if input1 == "1":
        menu_join_query()
    else:
        menu()

def menu_nest_query():
    print("1、根据旅游班次查导游信息")
    print("2、根据旅游班次查宾馆信息")
    print("3、根据班次查路线")
    print("4、根据团名查保险")
    s = input("请输入编号")
    s1 = input("请输入条件")
    query.nest_query(db, cursor, s, s1)
    input1 = input("输入1继续查询，否则退出")
    if input1 == "1":
        menu_nest_query()
    else:
        menu()


def menu_group_query():
    print("1、根据性别对导游分组")
    print("2、根据星级对宾馆分组")
    s = input("请输入编号")
    s1 = input("请输入条件")
    query.group_query(db,cursor,s,s1)
    input1 = input("输入1继续查询，否则退出")
    if input1 == "1":
        menu_group_query()
    else:
        menu()


def menu_view_query():
    print("1、根据导游编号查询该导游需带领的游客信息")
    print("2、根据游客姓名查询所属团号和导游信息")
    print("3、根据游客编号查询所属团号和导游信息")
    s = input("请输入编号")
    s1 = input("请输入条件")
    query.view_query(db, cursor, s, s1)
    input1 = input("输入1继续查询，否则退出")
    if input1 == "1":
        menu_view_query()
    else:
        menu()


def menu_transaction():
    db.ping(True)
    try:
        s = input("请输入需要修改的路线号")
        input2 = input("请输入修改后的终点")
        sql1 = 'update routes set destination=\"{input2}\" ' \
               'where route_id={s}'.format(s=s,input2=input2)
        cursor.execute(sql1)
        sql2 = 'select * from routes where route_id={s}'.format(s=s)
        input1 = input("请修改主要景点信息")
        sql3='update routes set main_attractions=\"{input1}\" ' \
               'where route_id={s}'.format(s=s,input1=input1)

        cursor.execute(sql3)
        db.commit()

        cursor.execute(sql2)
        fetchall2 = cursor.fetchall()
        print("commit操作后路线表的信息")
        for k in fetchall2:
            print(k)
    except:
        info = sys.exc_info()
        print("error")
        print(info[0], ":", info[1])
        db.rollback()

    input("输入任意键回到主菜单")
    menu()


menu()