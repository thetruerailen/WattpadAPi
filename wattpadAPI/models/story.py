from .chapter import Chapter

class Story:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data.get('description', '')
        self.cover_url = data.get('cover')
        self.url = data.get('url')
        self.read_count = data.get('readCount', 0)
        self.vote_count = data.get('voteCount', 0)
        self.comment_count = data.get('commentCount', 0)
        self.parts = [Chapter(ch) for ch in data.get('parts', [])]

    def __repr__(self):
        return f"<Story id={self.id} title='{self.title}'>"