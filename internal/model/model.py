from typing import Optional, List
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from internal.db.postgres import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.fullname!r})"
    
class Group(Base):
    __tablename__ = "groups"
     
     
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    closed: Mapped[bool]
    password: Mapped[str]
    items: Mapped[List["Item"]] = relationship(back_populates="group", cascade="all, delete-orphan")
    
    
    
class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    link: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    count: Mapped[int]
    cost: Mapped[str] = mapped_column(nullable=False)
    img: Mapped[str]
    
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates="items")
    
    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, name={self.name!r})"
    