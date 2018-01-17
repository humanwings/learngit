'''
sqlite3 多表查询，使用ORM框架(sqlalchemy)
参考：http://blog.csdn.net/Lotfee/article/details/57406450
      https://www.zhihu.com/question/38456789
'''

import random, datetime
import sqlalchemy

#from sqlalchemy import Column, Integer, Date, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
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

    # 建立与子表的关联， backref为子表建立与母表的关联属性runner
    times = relationship("Times", order_by="Times.value", backref="runner")

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

# 母子表参照检索
for runner in session.query(Runner).filter(Runner.id == "78807"):
    print(runner.id, " , ", runner.name, " , ", runner.dob)
    # 参照子表
    for time in runner.times:
        print(time.runner_id, " , ", time.value)
        # 反向参照母表
        print(time.runner.name)

# 关联检索
for runner, time in session.query(Runner,Times).filter(Runner.id == Times.runner_id).filter(Runner.id.like("%0%")).order_by(Times.value):
    print(runner.id, " --- ", time.value)

# 关联检索
for runner, time in session.query(Runner,Times).join(Times).filter(Runner.id == 621071).order_by(Times.value):
    print(runner.id, " --- ", time.value)

session.close()