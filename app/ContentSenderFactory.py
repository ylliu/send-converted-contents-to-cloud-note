from app.LocalSender import LocalSender
from app.UnsupportedSender import UnsupportedSender
from app.YuQueSender import YuQueSender


class ContentSenderFactory(object):
    def __init__(self, config):
        self.config = config

    def create(self):
        if self.config.save_type == "local":
            return LocalSender(self.config.token, self.config.file_path, self.config.format)
        elif self.config.save_type == "yuque":
            # 在这个namespace 和 上一个本地保存的file_path 这第二次参数定义不一样地方踩了好几次坑了
            return YuQueSender(self.config.token, self.config.namespace, self.config.format)
        else:
            print("不支持的类型，请检查config.json文件中save_type是否设置为local或者yuque")
            return UnsupportedSender(self.config.token, self.config.file_path, self.config.format)
