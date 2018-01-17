'''
sqlite3 增删改查，使用ORM框架(sqlalchemy)
参考： http://blog.csdn.net/Lotfee/article/details/57406450
'''

import random, datetime
import sqlalchemy

#from sqlalchemy import Column, Integer, Date, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:使用Declarative方法定义的映射类依据一个基类，这个基类是维系类和数据表关系的目录
Base = declarative_base()

# 定义User对象:
class Runner(Base):
    # 表的名字:
    __tablename__ = 'runner'

    # 表的结构:
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))
    dob = sqlalchemy.Column(sqlalchemy.Date)

class Times(Base):
    # 表的名字:
    __tablename__ = 'times'

    # 表的结构:
    runner_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('runner.id'),primary_key=True)
    value = sqlalchemy.Column(sqlalchemy.String(20), primary_key=True)

# 初始化数据库连接:
engine = sqlalchemy.create_engine('sqlite:///coachdata.sqlite',echo=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 这个定制的DBSession类会创建绑定到数据库的Session对象。
# 如果需要和数据库建立连接，只需要实例化一个DBSession
session = DBSession()

def listmenu():

    print("请选择操作内容：")
    print("1. 查询Runner表")
    print("2. 随机插入新数据")
    print("3. 随机删除数据")
    print("4. 随机更新数据")
    print("5. 退出")
    return input("\n输入选择：")

def select_runner(session):
    for runner in session.query(Runner).order_by(Runner.id):
        print(runner.id, " , ", runner.name, " , ", runner.dob)

def insert_runner(session):
    rid = random.randint(1, 1000000)
    rname = "runner_" + str(rid)
    new_runner = Runner(id = rid, name = rname, dob = datetime.datetime.today())
    session.add(new_runner)

    new_times = Times(runner_id = rid, value = random.uniform(13,17))
    session.add(new_times)
    new_times = Times(runner_id = rid, value = random.uniform(13,17))
    session.add(new_times)
    new_times = Times(runner_id = rid, value = random.uniform(13,17))
    session.add(new_times)

    session.commit()

def delete_runner(session):
    pass

def update_runner(session):
    pass

crud = {
    "1": select_runner,
    "2": insert_runner,
    "3": delete_runner,
    "4": update_runner,
    "5": lambda x: True
}

while True:

    result = crud[listmenu()](session)
    if result :
        break

session.close()

