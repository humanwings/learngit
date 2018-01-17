'''
sqlite3 单表查询进阶，使用ORM框架(sqlalchemy)
参考： http://blog.csdn.net/Lotfee/article/details/57406450
'''

import random, datetime
import sqlalchemy

#from sqlalchemy import Column, Integer, Date, String, create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

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

# 初始化数据库连接:
engine = sqlalchemy.create_engine('sqlite:///coachdata.sqlite',echo=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 这个定制的DBSession类会创建绑定到数据库的Session对象。
# 如果需要和数据库建立连接，只需要实例化一个DBSession
session = DBSession()

# 排序order by
for runner in session.query(Runner).order_by(Runner.id):
    print(runner.id, " , ", runner.name, " , ", runner.dob)

# 查询部分列
for id, name in session.query(Runner.id, Runner.name):
    print(id, " , ", name)

# 给列起别名
for row in session.query(Runner.name.label("name_label")):
    print(row.name_label)

# 切片查询部分行
for runner in session.query(Runner).order_by(Runner.id)[1:3]:
    print(runner.id, " , ", runner.name, " , ", runner.dob)

# 条件查询AND
for runner in session.query(Runner).filter(Runner.name.like("%0%"), Runner.dob == "2017-11-22"):
    print(runner.id, " , ", runner.name, " , ", runner.dob)

# 条件查询OR
for runner in session.query(Runner).filter(sqlalchemy.or_(Runner.name.like("%0%"), Runner.dob == "2017-11-22")):
    print(runner.id, " , ", runner.name, " , ", runner.dob)

# 取得第一条
runner = session.query(Runner).order_by(Runner.id).first()
print(runner.id, " , ", runner.name, " , ", runner.dob)

# 取得一条数据（无数据产生NoResultFound， 多条数据产生MultipleResultsFound）
runner = session.query(Runner).filter(sqlalchemy.and_(Runner.name.like("%40050%"))).one()
print(runner.id, " , ", runner.name, " , ", runner.dob)

# 参数指定
for runner in session.query(Runner).filter(text("id<:value ")).params(value=300000):
    print(runner.id, " , ", runner.name, " , ", runner.dob)

# 计数
ct = runner = session.query(Runner).order_by(Runner.id).count()
print(ct)

session.close()

