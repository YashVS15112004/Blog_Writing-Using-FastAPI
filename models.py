from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey("Users.id"))
    creator = relationship("User",back_populates="blogs")

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)
    blogs = relationship('Blog',back_populates="creator")
