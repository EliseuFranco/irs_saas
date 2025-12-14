from flask import jsonify

class ResponseDto:
    def __init__(self, status, content, message):
        self.status = status
        self.content = content
        self.message = message

    
    def to_json(self):
        return {
            'status': self.status,
            'content': self.content,
            'message': self.message
        }