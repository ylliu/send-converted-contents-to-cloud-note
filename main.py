# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from app.ConfigReader import ConfigReader
from app.ContentSenderFactory import ContentSenderFactory
from app.RecordConvertService import RecordConvertService
from app.XunFeiConvertor import XunFeiConvertor


def convert_record_and_send_out(config_file):
    config = ConfigReader(config_file).read_auth()
    record_convertor = XunFeiConvertor(config.appid, config.secret_key)
    sender = ContentSenderFactory(config).create()
    record_convert_service = RecordConvertService(record_convertor, sender, config.file_path)
    record_convert_service.send_converted_contents_to_cloud_note()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_record_and_send_out("config.json")
    os.system("pause")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
