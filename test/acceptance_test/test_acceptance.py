import json
import shutil
import unittest

from app.ConfigReader import ConfigReader
from app.RecordConvertService import RecordConvertService
from app.XunFeiConvertor import XunFeiConvertor
from app.YuQueSender import YuQueSender


class AcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()
        record_convertor = XunFeiConvertor(self.config.appid, self.config.secret_key)
        sender = YuQueSender(self.config.token, self.config.namespace, self.config.format)
        self.record_convert_service = RecordConvertService(record_convertor, sender, self.config.file_path)

    def test_should_convert_record_and_send_to_cloud_note(self):
        response = self.record_convert_service.convert("D:/ylliu/tz/record_for_test/3.m4a")
        json_data = json.loads(response)
        self.assertEqual("喂喂喂喂喂喂喂喂。", json_data["data"]["body"])
        self.assertEqual("3", json_data["data"]["title"])

    # this test call real service, it will consume hours of service
    def disabled_test_should_convert_record_and_send_their_contents_to_cloud_note(self):
        self.record_convert_service.send_converted_contents_to_cloud_note()
        case_dir = "D:/ylliu/tz/record_base_file/"
        files_to_be_recover = [case_dir + "1.mp3",
                               case_dir + "3.m4a",
                               case_dir + "9-12-中文名字.mp3",
                               case_dir + "9.mp3"]
        for file in files_to_be_recover:
            shutil.copy(file, self.config.file_path)
