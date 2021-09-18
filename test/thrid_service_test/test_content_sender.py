import json
import os
import unittest

from app.ConfigReader import ConfigReader
from app.LocalSender import LocalSender
from app.StubSender import StubSender
from app.YuQueSender import YuQueSender


class ContentSenderTest(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()
        self.title = "测试的标题1"
        self.body = "测试的内容"

    def test_should_send_content_to_cloud_note(self):
        self.config.save_type = "yuque"
        self.content_sender = YuQueSender(self.config.token, self.config.namespace, self.config.format)
        response = self.content_sender.send(self.title, self.body)
        json_data = json.loads(response)
        print(json_data)
        self.assertEqual(True, self.body in json_data["data"]["body"])
        self.assertEqual(self.title, json_data["data"]["title"])

    def test_should_save_converted_contents_to_local_machine(self):
        self.config.save_type = "local"
        saved_file = self.config.file_path + self.title + ".txt"
        if os.path.exists(saved_file):
            os.remove(saved_file)
        # send to local file use namespace as local path
        self.content_sender = LocalSender(self.config.token, self.config.file_path, self.config.format)
        self.content_sender.send(self.title, self.body)
        self.assertTrue(os.path.exists(saved_file))
        with open(saved_file, "r", encoding='utf-8') as f:
            data = f.readline()
        self.assertEqual(self.body, data)
        os.remove(saved_file)

    # Do I need to test test sub
    def test_should_send_content_using_test_stub(self):
        self.content_sender = StubSender("token", "namespace", "format")
        json_data = self.content_sender.send(self.title, self.body)
        self.assertEqual(self.body, json_data["data"]["body"])
        self.assertEqual(self.title, json_data["data"]["title"])
