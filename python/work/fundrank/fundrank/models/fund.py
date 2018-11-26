from sqlalchemy import (
    Column,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
    Date,
    Enum,
    Float
)

import enum

from .meta import Base

# class FundTypeEnum(enum.Enum):
#     stock   = 1
#     mix     = 2
#     index   = 3

# class FundStyleEnum(enum.Enum):
#     value   = 1
#     growth  = 2
#     balance = 3

class Fund(Base):
    __tablename__ = 'fund'
    code = Column(String(6), primary_key=True)
    name = Column(Text)
    type = Column(Integer)
    style = Column(Integer)
    start_date = Column(Date)
    manager = Column(String(4))
    manager_date = Column(Date)
    scale = Column(Integer)
    mng_rate = Column(Float)
    dps_rate = Column(Float)
