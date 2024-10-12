from sqlalchemy import create_engine
from models import BaseModel


DB_URL = 'sqlite:///MotoristBot.db'
engine = create_engine(DB_URL, echo=True)

BaseModel.metadata.create_all(engine)
