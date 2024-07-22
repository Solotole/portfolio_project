#!/usr/bin/pyhton3
""" API routes dor the chat room """
from flask import Flask, request, jsonify, abort
from models import storage
from models.chatmessages import ChatMessage
from models.user import User 
from api.v1.views import app_views

@app_views.route('/messages', methods=['POST'], strict_slashes=False)
def send_message():
    """Endpoint to send a message"""
    user_id = request.json.get('user_id')
    message = request.json.get('message')
    print(user_id)
    
    if not user_id or not message:
        abort(400, description="user_id and message are required")

    new_message = ChatMessage(user_id=user_id, message=message)
    storage.new(new_message)
    storage.save()

    return jsonify(new_message.to_dict()), 201

@app_views.route('/messages', methods=['GET'], strict_slashes=False)
def get_messages():
    """Endpoint to get all messages"""
    messages = storage.all(ChatMessage)
    users = storage.all(User)
    user_id_to_username = {user.id: user.first_name for user in users.values()}
    
    # Attach the username to each message
    for message in messages.values():
        if message.user_id in user_id_to_username:
            message.username = user_id_to_username[message.user_id]
    
    sorted_messages = sorted(messages.values(), key=lambda msg: msg.created_at)
    # return jsonify([message.to_dict() for message in messages.values()])
    return jsonify([message.to_dict() for message in sorted_messages])