import abc


class RecordConvertor(object):
    def __init__(self, appid, secret_key):
        self.appid = appid
        self.secret_key = secret_key

    @abc.abstractmethod
    def convert(self, upload_file_path):
        pass
