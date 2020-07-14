from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('mysql://root:@localhost/academic', convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

class User(Base):
    __table__ = Base.metadata.tables['user']

class Course(Base):
    __table__ = Base.metadata.tables['course']


# if __name__ == '__main__':
#     from sqlalchemy.orm import scoped_session, sessionmaker, Query
#     db_session = scoped_session(sessionmaker(bind=engine))
#     for item in db_session.query(User.user_id, User.username):
#         print(item)