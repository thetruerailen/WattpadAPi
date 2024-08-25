from datetime import datetime
from .user import User

class CommentId:
    def __init__(self, data):
        self.namespace = data.get('namespace')
        self.resource_id = data.get('resourceId')

class Resource:
    def __init__(self, data):
        self.namespace = data.get('namespace')
        self.resource_id = data.get('resourceId')

class Comment:
    def __init__(self, data):
        self.resource = Resource(data.get('resource', {}))
        self.user = User(data.get('user', {}))
        self.comment_id = CommentId(data.get('commentId', {}))
        self.text = data.get('text', '')
        self.created = datetime.fromisoformat(data.get('created', '').replace('Z', '+00:00'))
        self.modified = datetime.fromisoformat(data.get('modified', '').replace('Z', '+00:00'))
        self.status = data.get('status', '')
        self.sentiments = data.get('sentiments', {})
        self.reply_count = data.get('replyCount', 0)
        self.labels = data.get('labels', [])
        self.deeplink = data.get('deeplink', '')

    def __repr__(self):
        return f"<Comment id={self.comment_id.resource_id} user='{self.user.name}'>"

class CommentsPagination:
    def __init__(self, data):
        self.after = CommentId(data.get('after', {}))

class CommentsResponse:
    def __init__(self, data):
        self.pagination = CommentsPagination(data.get('pagination', {}))
        self.comments = [Comment(comment_data) for comment_data in data.get('comments', [])]