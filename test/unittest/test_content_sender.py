import json
import unittest

from app.ConfigReader import ConfigReader
from app.StubSender import StubSender
from app.YuQueSender import YuQueSender


class ContentSenderTest(unittest.TestCase):
    # the true service where to place it
    def test_should_send_content_to_cloud_note(self):
        body = "我是需要被写入的内容100%200%"
        title = "测试的标题7"
        config = ConfigReader("../../config.json").read_auth()
        self.content_sender = YuQueSender(config.token, config.namespace, config.format)
        response = self.content_sender.send(title, body)
        json_data = json.loads(response)
        print(json_data)
        self.assertEqual(True, body in json_data["data"]["body"])
        self.assertEqual(title, json_data["data"]["title"])

    def test_should_send_content_using_test_stub(self):
        body = "我是需要被写入的内容"
        title = "测试的标题2"
        self.content_sender = StubSender("token", "namespace", "format")
        json_data = self.content_sender.send(title, body)
        self.assertEqual(body, json_data["data"]["body"])
        self.assertEqual(title, json_data["data"]["title"])
