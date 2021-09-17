import json
import os
import shutil
import unittest

from app.ConfigReader import ConfigReader
from app.LocalSender import LocalSender
from app.RecordConvertService import RecordConvertService
from app.XunFeiConvertor import XunFeiConvertor
from app.YuQueSender import YuQueSender


class AcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()
        self.record_convertor = XunFeiConvertor(self.config.appid, self.config.secret_key)
        self.test_file = "D:/ylliu/tz/record_for_test/3.m4a"
        self.body = "喂喂喂喂喂喂喂喂。"

    def test_should_convert_record_and_send_to_cloud_note(self):
        sender = YuQueSender(self.config.token, self.config.namespace, self.config.format)
        self.record_convert_service = RecordConvertService(self.record_convertor, sender, self.config.file_path)
        response = self.record_convert_service.convert(self.test_file)
        json_data = json.loads(response)
        self.assertEqual(self.body, json_data["data"]["body"])
        self.assertEqual("3", json_data["data"]["title"])

    def test_should_convert_record_and_send_to_local_file(self):
        saved_file = self.test_file.split(".")[0] + ".txt";
        print(saved_file)
        if os.path.exists(saved_file):
            os.remove(saved_file)
        # I need to use namespace as file_path when save to local file(bad smell) 这里的test.file
        # 两个文件夹也是个坏味道然后从别的地方拷贝数据也要想想怎么处理
        sender = LocalSender(self.config.token, "D:/ylliu/tz/record_for_test/", self.config.format)
        self.record_convert_service = RecordConvertService(self.record_convertor, sender, self.config.file_path)
        response = self.record_convert_service.convert(self.test_file)
        self.assertTrue(os.path.exists(saved_file))
        with open(saved_file, "r", encoding='utf-8') as f:
            data = f.readline()
        self.assertEqual(self.body, data)

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
