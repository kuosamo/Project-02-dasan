# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime
from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker
from model import Dasan

# 서버연결
server = 'ec2-52-78-188-213.ap-northeast-2.compute.amazonaws.com'
connection_string = 'mysql+mysqldb://root:wpeo1108@{}:3306/dasan'.format(server)
engine = create_engine(connection_string, pool_recycle = 3600, encoding='utf-8')
Session = sessionmaker(bind=engine)

class DasanDAO(object):
    def __init__(self):
        pass

    # 크롤링한 데이터를 DB에 저장
    def dasan_db(self, question, directory):
        session = Session()

        # crawler에서 넘겨받은 인자를 Mysql DB에 저장
        call = Dasan(question = question, directory = directory,
                                            crawl_time = datetime.datetime.now())
        session.add(call)
        session.commit()

        session.close()
        
    # DB의 데이터에서 keyword검색
    def select_in_question(self, keyword):
        data = []
        session = Session()
        result = session.query(Dasan).filter(Dasan.question.like('%' + keyword + '%')).all()

        for row in result:
            search = {}
            search['question'] = row.question
            search['directory'] = row.directory

            data.append(search)
        return data
