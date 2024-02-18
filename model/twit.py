from model.user import User
class Twit:
    def __init__(self, id: int, body: str, author: User):
        self.body = body
        self.author = author
        self.id = id