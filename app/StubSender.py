from app.ContentSender import ContentSender


class StubSender(ContentSender):

    def __init__(self, token, namespace, format):
        super().__init__(token, namespace, format)

    def send(self, title, body):
        data = {
            'data': {'body': body, 'title': title}
        }
        return data
