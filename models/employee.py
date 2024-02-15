from sqlalchemy import Integer, Column, String

from config.database import Base, engine


class Employee(Base):
    __tablename__ = 'emp'
    id = Column(Integer, primary_key=True, index=True)
    employee_name = Column(String, index=True)
    phone_number = Column(String, index=True)
    age = Column(Integer, index=True)


Base.metadata.create_all(bind=engine)