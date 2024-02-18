from sqlalchemy import Column,Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, validates

Base = declarative(Base):