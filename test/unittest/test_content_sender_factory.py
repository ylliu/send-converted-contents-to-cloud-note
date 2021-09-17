import unittest

from app.Config import Config
from app.ContentSenderFactory import ContentSenderFactory
from app.LocalSender import LocalSender
from app.UnsupportedSender import UnsupportedSender
from app.YuQueSender import YuQueSender


class ContentSenderFactoryTest(unittest.TestCase):
    def test_should_create_content_sender_type_form_config(self):
        config = Config("", "", "", "", "", "", "local")
        content_sender = ContentSenderFactory(config).create()
        self.assertIsInstance(content_sender, LocalSender)

        config = Config("", "", "", "", "", "", "yuque")  
        content_sender = ContentSenderFactory(config).create()
        self.assertIsInstance(content_sender, YuQueSender)

        config = Config("", "", "", "", "", "", "none")
        content_sender = ContentSenderFactory(config).create()
        self.assertIsInstance(content_sender, UnsupportedSender)
