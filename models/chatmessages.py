#!/usr/bin/python3
from sqlalchemy import Column, String, Text, ForeignKey
from models.base_model import BaseModel, Base


# user's chat messages storage class
class ChatMessage(BaseModel, Base):
    __tablename__ = 'chat_messages'

    # user's unique id
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    # message sent by user
    message = Column(Text, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Book class initialization special method """
        # addressing BaseModel __init__magic method
        super().__init__(*args, **kwargs)
