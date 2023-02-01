from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from mytables.my_database import Base


class Number(Base):
    __tablename__ = 'numbers'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)
    name = relationship('Name')

    def __repr__(self):
        return f"Группа (ID: {self.id}, Название: {self.group_name}, Название группы: {self.lesson_title})"
