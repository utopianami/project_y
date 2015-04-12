from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import logging

# logging.basicConfig()
# logging.getLogger('sqlalchemy.pool').setLevel(logging.DEBUG)

 #'mysql://id:password@localhost/database_name',
engine = create_engine('mysql://dbuser:dkagh123@localhost/projecty', convert_unicode=True,
                       pool_recycle=500, pool_size=250, max_overflow=20, echo=False, echo_pool=True )
# engine = create_engine('mysql://dbuser:dkagh123@localhost/projecty', convert_unicode=True,
#                        pool_recycle=500, pool_size=250, max_overflow=20, echo=False, echo_pool=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
 
Base = declarative_base()
Base.query = db_session.query_property()
 
def init_db():
    Base.metadata.create_all(bind=engine)
