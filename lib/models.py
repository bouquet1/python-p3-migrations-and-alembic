
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, create_engine, desc
from sqlalchemy.orm import declarative_base
#from sqlalchemy.ext.declarative import declarative_base (same as the line above)

engine = create_engine('sqlite:///migrations_test.db')

#define the Base class
Base = declarative_base()

#Define a Student class and inherit from Base
class Student(Base):
    #define the table name using __tablename__
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"



