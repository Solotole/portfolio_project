#!/usr/bin/python3
from sqlalchemy import Column, String, Text, ForeignKey
from models.base_model import BaseModel, Base

class ChatMessage(BaseModel, Base):
    __tablename__ = 'chat_messages'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    message = Column(Text, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Book class initialization special method """
        super().__init__(*args, **kwargs)