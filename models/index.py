

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from config.db import Base
    
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False)
    email= Column(String(80), nullable=False, unique=True)
    def __repr__(self):
        return 'ItemModel(name=%s)' % (self.name)