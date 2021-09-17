# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from app.ConfigReader import ConfigReader
from app.LocalSender import LocalSender
from app.RecordConvertService import RecordConvertService
from app.XunFeiConvertor import XunFeiConvertor
from app.YuQueSender import YuQueSender


def convert_record_and_send_to_cloud_app():
    config = ConfigReader("config.json").read_auth()
    record_convertor = XunFeiConvertor(config.appid, config.secret_key)
    if config.save_type == "local":
        sender = LocalSender(config.token, config.file_path, config.format)
    else:
        sender = YuQueSender(config.token, config.namespace, config.format)

    record_convert_service = RecordConvertService(record_convertor, sender, config.file_path)
    file_paths = record_convert_service.get_supported_audio_files_from()
    for file_path in file_paths:
        record_convert_service.convert(file_path)
        # 删除文件，防止出现忘记删除文件，导致重新识别浪费转写服务时长
        os.remove(file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_record_and_send_to_cloud_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
