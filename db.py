#!/usr/bin/env python
# -*-coding=utf-8-*-

import os
from sqlalchemy import Column, Integer
from sqlalchemy import String, Float, create_engine
from sqlalchemy.orm import sessionmaker, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

# 创建对象的基类:
Base = declarative_base()

# 定义company对象:
class Company(Base):
    # 表的名字:
    __tablename__ = 'companies'
    __table_args__ = (
        UniqueConstraint('code', name='uniq_companies0name'),
    )
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(6),  nullable=False)
    name = Column(String(16), nullable=False)
    zz1code = Column(String(2), nullable=True)
    zz1name = Column(String(16), nullable=True)
    zz2code = Column(String(4), nullable=True)
    zz2name = Column(String(16), nullable=True)
    zz3code = Column(String(6), nullable=True)
    zz3name = Column(String(48), nullable=True)

# 初始化数据库连接:
engine = create_engine('sqlite:///company.db')
Base.metadata.create_all(engine)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def add_data(records):
    # 创建session对象:
    session = DBSession()
    for record in records:
        # 添加到session:
        session.add(record)
    # 提交即保存到数据库:
    try:
        session.commit()
    except exc.IntegrityError:
        print 'exist...'
    # 关闭session:
    session.close()

def get_company(code):
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    try:
        company = session.query(Company).filter(Company.code==code).one()
        print 'company name:', company.name
    except exc.NoResultFound:
        company = None
    finally:
        # 关闭Session:
        session.close()
    return company

def get_company_by_zzcode(code):
    codes = []
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    try:
        company = session.query(Company).filter(Company.zz2code==code).all()
    except exc.NoResultFound:
        company = None
    finally:
        # 关闭Session:
        session.close()
    for c in company:
        codes.append(c.code)
    return codes

def create_company():
    datadir = '/home/li/company'
    scope_file='/home/code/future/stocks_data.txt'
    sf = open(scope_file, 'r')
    scope_codes = str(sf.readlines())
    sf.close()
    files = os.listdir(datadir)
    for fname in files:
        if fname.split('.')[0] not in scope_codes:
            continue
        with open(os.path.join(datadir,fname),'r') as f:
           # read file end
           f.seek(2)
           data = f.readline().strip('\n')
           data = data.strip().split(',')
           print data[1], data[2]
           company = Company()
           company.code = str(data[1]).zfill(6)
           company.name = str(data[2]).decode('utf-8')
           company.zz1code = str(data[3]).zfill(2)
           company.zz1name = str(data[4]).decode('utf-8')
           company.zz2code = str(data[5]).zfill(4)
           company.zz2name = str(data[6]).decode('utf-8')
           company.zz3code = str(data[7]).zfill(6)
           company.zz3name = str(data[8]).decode('utf-8')
           if not get_company(company.code):
               add_data([company])

if __name__ == '__main__':
    #create_company()
    data = get_company_by_zzcode('0201')
    print data
