from typing import List, Optional

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base

course_lesson_association = Table(
    'user_group_association',
    Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('lesson_id', Integer, ForeignKey('lessons.id'))
)


class Courses(Base):
    __tablename__ = 'courses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[int]]

    lessons: Mapped[List["Lessons"]] = relationship(
        secondary=course_lesson_association
    )
