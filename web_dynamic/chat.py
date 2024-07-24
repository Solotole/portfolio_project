#!/usr/bin/python3
""" chat module """
from flask import Blueprint, render_template, session

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat/<user_id>')
def chat(user_id):
    """ chat method rendering html
        Args:
            user_id: id belongng to user
        Return:
            return a rendered chat.html
    """
    return render_template('chat.html', user_id=user_id)
