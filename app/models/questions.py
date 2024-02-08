from random import shuffle
from typing import List, Optional

from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base

class Questions(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    type: Mapped[str] = mapped_column(default='quiz')
    img: Mapped[Optional[str]]

    answers: Mapped[List['Answers']] = relationship()