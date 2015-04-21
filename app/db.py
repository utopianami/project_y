from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool


engine = create_engine('mysql://dbuser:dkagh123@localhost/projecty', convert_unicode=True, poolclass=NullPool,pool_size=1)

db_session = scoped_session(sessionmaker(expire_on_commit=False, autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
 
def init_db():
    Base.metadata.create_all(bind=engine)
