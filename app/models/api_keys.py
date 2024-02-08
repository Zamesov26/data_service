import uuid

from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class APIKeys(Base):
    __tablename__ = 'api_keys'

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(default=lambda: str(uuid.uuid4()))
    is_active: Mapped[bool] = mapped_column(default=True)
