class Chapter:
  def __init__(self, data):
      self.id = data['id']
      self.title = data['title']
      self.url = data.get('url')
      self.create_date = data.get('createDate')
      self.modify_date = data.get('modifyDate')
      self.read_count = data.get('readCount', 0)
      self.vote_count = data.get('voteCount', 0)
      self.comment_count = data.get('commentCount', 0)

  def __repr__(self):
      return f"<Chapter id={self.id} title='{self.title}'>"