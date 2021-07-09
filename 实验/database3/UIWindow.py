import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# 导入designer工具生成的login模块

from ui import main
from ui.admin import Ui_admin
from ui.guide import Ui_guide
from ui.hotel import Ui_hotel
from ui.main import Ui_main
from ui.tourist import Ui_tourist
from ui.tourist_info import Ui_tourist_info


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


class main(QWidget, Ui_main):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

class hotel(QWidget,Ui_hotel):
    def __init__(self):
        super(hotel,self).__init__()
        self.setupUi(self)

class tourist(QWidget,Ui_tourist):
    def __init__(self):
        super(tourist,self).__init__()
        self.setupUi(self)

class guide(QWidget,Ui_guide):
    def __init__(self):
        super(guide,self).__init__()
        self.setupUi(self)

class admin(QWidget,Ui_admin):
    def __init__(self):
        super(admin,self).__init__()
        self.setupUi(self)

class tourist_info(QWidget,Ui_tourist_info):
    def __init__(self):
        super(tourist_info,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app =QApplication(sys.argv)
    m = main()
    m.show()
    h = hotel()
    t = tourist()
    g = guide()
    a = admin()

    ti = tourist_info()


    def getTouristInfo():
        text = ti.lineEdit.text()

        query.view_query(db, cursor, "3", text)


    m.pushButton_3.clicked.connect(
        lambda :{m.close(),h.show()}
    )

    m.pushButton_4.clicked.connect(
        lambda :{m.close(),t.show()}
    )

    m.pushButton_5.clicked.connect(
        lambda :{m.close(),g.show()}
    )

    m.pushButton_6.clicked.connect(
        lambda :{m.close(),a.show()}
    )

    h.pushButton.clicked.connect(
        lambda :{h.close(),m.show()}
    )

    t.pushButton_3.clicked.connect(
        lambda :{t.close(),m.show()}
    )

    g.pushButton_3.clicked.connect(
        lambda :{g.close(),m.show()}
    )

    a.pushButton_3.clicked.connect(
        lambda :{a.close(),m.show()}
    )

    t.pushButton.clicked.connect(
        lambda :{t.close(),ti.show()}
    )

    ti.pushButton_3.clicked.connect(
        lambda :{ti.close(),t.show()}
    )

    ti.pushButton.clicked.connect(getTouristInfo)



    sys.exit(app.exec_())