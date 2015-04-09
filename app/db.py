from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


 #'mysql://id:password@localhost/database_name',
#engine = create_engine('mysql://dbtest:dkagh123@localhost/projecty', convert_unicode=True)
engine = create_engine('mysql://dbuser:dkagh123@localhost/projecty', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
 
Base = declarative_base()
Base.query = db_session.query_property()
 
def init_db():
    Base.metadata.create_all(bind=engine)
