import os
import shutil
import unittest

from app.ConfigReader import ConfigReader
from app.RecordConvertService import RecordConvertService
from app.StubConvertor import StubConvertor
from app.StubSender import StubSender


class RecordConvertServiceTest(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()
        record_convertor = StubConvertor(self.config.appid, self.config.secret_key)
        sender = StubSender(self.config.token, self.config.namespace, self.config.format)

        self.record_convert_service = RecordConvertService(record_convertor, sender, self.config.file_path)

        case_dir = "../test_audio/"
        files_to_be_copied = [case_dir + "1.mp3",
                              case_dir + "3.m4a",
                              case_dir + "9-12-中文名字.mp3",
                              case_dir + "9.mp3"]
        for file in files_to_be_copied:
            shutil.copy(file, self.config.file_path)

    def tearDown(self):
        files = self.record_convert_service.get_supported_audio_files_from()
        for file in files:
            os.remove(file)

    def test_get_supported_audio_files_from_path(self):
        files_expected = [self.config.file_path + "1.mp3",
                          self.config.file_path + "3.m4a",
                          self.config.file_path + "9-12-中文名字.mp3",
                          self.config.file_path + "9.mp3"]
        print(files_expected)
        files = self.record_convert_service.get_supported_audio_files_from()
        print(files)
        self.assertCountEqual(files_expected, files)

    def test_should_extract_file_name_from_file_path(self):
        self.assertEqual("1",
                         self.record_convert_service.extract_file_name_form(self.config.file_path + "1.mp3"))
        self.assertEqual("9-12-中文名字",
                         self.record_convert_service.extract_file_name_form(
                             self.config.file_path + "9-12-中文名字.mp3"))

    def test_should_convert_record_and_send_out(self):
        json_response = self.record_convert_service.convert(self.config.file_path + "9-12-中文名字.mp3")

        self.assertEqual("喂喂喂喂喂喂喂喂。", json_response["data"]["body"])
        self.assertEqual("9-12-中文名字", json_response["data"]["title"])
