# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)  # Longitud máxima de 50 caracteres
    email = Column(String(255), unique=True, index=True)  # Longitud máxima de 255 caracteres
