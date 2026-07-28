import pymysql
db=pymysql.connect(user='root', password="" ,host="localhost",database="distracted_drivers")

def selectone(data):
    cu=db.cursor()
    cu.execute(data)
    d=cu.fetchone()
    return d
def insert(data):
    cu=db.cursor()
    cu.execute(data)
    db.commit()
def selectall(data):
    cu=db.cursor()
    cu.execute(data)
    d=cu.fetchall()
    return d
def update(data):
    cu=db.cursor()
    cu.execute(data)
    db.commit()
def delete(data):
    cu=db.cursor()
    cu.execute(data)
    db.commit()