import pymysql
import datetime

# create functions that interact with the database

def find_name_password(name, password):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_users where usr_name = \'{name_value}\' and usr_password = \'{password_value}\';".format(
            name_value=name,
            password_value=password)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def find_user(name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_users where usr_name = \'{name_value}\';".format(name_value=name)
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None

def add_user(name, password):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "insert into app01_users(usr_name, usr_password, usr_type) value " \
              "(\'{name_value}\', \'{password_value}\', \'{type_value}\');".format(name_value=name,
                                                                                   password_value=password,
                                                                                   type_value=1)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def add_worker(id, name, sex, age, department, position, phone):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "insert into app01_worker(worker_id, worker_name, worker_sex, worker_age," \
              "worker_department, worker_position, worker_phone, worker_entry_time) value " \
              "(\'{id}\', \'{name}\', \'{sex}\', \'{age}\', \'{department}\', \'{position}\', " \
              "\'{phone}\', \'{entry_time}\');".format(id=id, name=name, sex=sex, age=age,
                                                      department=department, position=position,
                                                      phone=phone, entry_time=datetime.datetime.now())
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def delete_worker(id):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "delete from app01_worker where worker_id = \'{id}\';".format(id=id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False

def find_all_workers():
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_worker;"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def find_worker_by_name(name):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_worker where worker_name = \'{name_value}\';".format(name_value=name)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def find_worker_by_department(department):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_worker where worker_department = \'{department_value}\';".format(department_value=department)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def find_worker_by_position(position):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "select * from app01_worker where worker_position = \'{position_value}\';".format(position_value=position)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def modify_worker(id, name, sex, age, department, position, phone, entry_time):
    try:
        db = pymysql.connect(host='localhost', user='root',
                             password='xyl1278157445', port=3306, db='djangodemo')
        cursor = db.cursor()
        sql = "update app01_worker set worker_name=\'{name}\', worker_sex=\'{sex}\'," \
              "worker_age=\'{age}\', worker_department=\'{department}\', worker_position=\'{position}\'," \
              "worker_phone=\'{phone}\', worker_entry_time=\'{entry_time}\' where worker_id=\'{id}\';".format(name=name,
                 sex=sex, age=age, department=department, position=position, phone=phone, entry_time=entry_time, id=id)
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return False


