from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from mytables.my_database import Base

association_table = Table('association', Base.metadata, Column('lesson_id', Integer, ForeignKey('lessons.id')),
                          Column('group_id', Integer, ForeignKey('numbers.id')))


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = Column(String(250), nullable=False)
    groups = relationship("Number", secondary=association_table, backref='group_lesson')

    def __repr__(self):
        return f"Предмет (ID: {self.id}, Название: {self.lesson_title})"