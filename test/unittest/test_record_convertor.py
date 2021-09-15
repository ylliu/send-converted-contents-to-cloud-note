import unittest

from app.ConfigReader import ConfigReader
from app.StubConvertor import StubConvertor
from app.XunFeiConvertor import XunFeiConvertor


class RecordConvertorTest(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()

    # where to place real service test
    def test_get_record_convert_result(self):
        record_convertor = XunFeiConvertor(self.config.appid, self.config.secret_key)
        with open("../BaseContent.txt", "r", encoding='utf-8') as file:
            content_expected = str(file.readlines()).replace("'", "")
            content = record_convertor.convert(self.config.file_path + "/3.m4a")
            self.assertEqual(content_expected, str(content))

    def test_get_record_convert_result_using_stub(self):
        with open("../BaseContent.txt", "r", encoding='utf-8') as file:
            content_expected = str(file.readlines()).replace("'", "")

            self.record_convertor = StubConvertor(self.config.appid, self.config.secret_key)
            content = self.record_convertor.convert(self.config.file_path + "/3.m4a")
            self.assertEqual(content_expected, str(content))
