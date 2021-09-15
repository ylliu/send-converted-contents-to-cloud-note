from app.RecordConvertor import RecordConvertor


class StubConvertor(RecordConvertor):
    def __init__(self, appid, secret_key):
        super().__init__(appid, secret_key)

    def convert(self, upload_file_path):
        return '[{"bg":"540","ed":"3070","onebest":"喂喂喂喂喂喂喂喂。","speaker":"0"}]'
