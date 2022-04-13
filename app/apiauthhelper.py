from functools import wraps
from flask import request, jsonify

from app.models import User

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else:
            return {
                'status': 'not ok',
                'message': "Missing header. Please add the header 'x-access-token' to your headers."
            }
        if not token:
            return {
                'status': 'not ok',
                'message': "Missing authentication token."
            }
        user = User.query.filter_by(apitoken=token).first()
        if not user:
            return {
                'status': 'not ok',
                'message': 'That token does not belong to valid user.'
            }
        return func(*args, **kwargs)
    return decorated