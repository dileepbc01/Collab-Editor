from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import types,text
from . import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[types.UUID] = mapped_column( types.Uuid, primary_key=True, index=True,server_default=text("gen_random_uuid()") )
    email: Mapped[str] = mapped_column(index=True, unique=True)
    fullname: Mapped[str]
    hashed_password: Mapped[str]