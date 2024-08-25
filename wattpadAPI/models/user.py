class User:
  def __init__(self, data):
      self.name = data.get('name', '')
      self.avatar = data.get('avatar', '')

  def __repr__(self):
      return f"<User name='{self.name}'>"