import abc


class ContentSender(object):
    def __init__(self, token, namespace, format):
        self.token = token
        self.namespace = namespace
        self.format = format

    @abc.abstractmethod
    def send(self, title, body):
        pass
