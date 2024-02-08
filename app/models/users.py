from typing import Optional, Any

from sqlalchemy import JSON, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    hashed_password: Mapped[Optional[str]]
    telegram_id: Mapped[Optional[str]]

    def __str__(self):
        return f'(<Users> id_={self.id}, name={self.name})'

    def __repr__(self):
        return self.__str__()
