from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./crisis.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    name = Column(String)       # e.g. "City Shelter"
    type = Column(String)       # e.g. "shelter", "hospital"
    address = Column(String)
    lat = Column(Float)
    lng = Column(Float)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    title = Column(String)      # e.g. "Flood Warning"
    description = Column(String)
    severity = Column(String)   # "low", "medium", "high"

Base.metadata.create_all(bind=engine)