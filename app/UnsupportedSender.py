from app.ContentSender import ContentSender


class UnsupportedSender(ContentSender):
    def __init__(self, token, namespace, format):
        super().__init__(token, namespace, format)

    def send(self, title, body):
        pass