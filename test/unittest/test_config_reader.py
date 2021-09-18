import json
import os
import unittest

from app.ConfigReader import ConfigReader



class ConfigReaderTest(unittest.TestCase):
    def test_should_return_config_info(self):
        # the config.json should be created by test
        config = {
            "appid": "123123",
            "secret_key": "key3432423",
            "token": "tokenerywirwe",
            "namespace": "namespace3398hffsd",
            "format": "html",
            "file_path": "D:/ylliu/tz/record/",
            "save_type": "yuque"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        config = ConfigReader("../../config_test.json").read_auth()
        self.assertEqual(config.appid, "123123")
        self.assertEqual(config.secret_key, "key3432423")
        self.assertEqual(config.token, "tokenerywirwe")
        self.assertEqual(config.namespace, "namespace3398hffsd")
        self.assertEqual(config.format, "html")
        self.assertEqual(config.file_path, "D:/ylliu/tz/record/")
        self.assertEqual(config.save_type, "yuque")
        os.remove("../../config_test.json")

    def test_should_set_run_path_as_file_path_when_fule_path_is_empty(self):
        config = {
            "appid": "123123",
            "secret_key": "key3432423",
            "token": "tokenerywirwe",
            "namespace": "namespace3398hffsd",
            "format": "html",
            "file_path": "",
            "save_type": "yuque"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        config = ConfigReader("../../config_test.json").read_auth()

        self.assertEqual(config.file_path, os.getcwd()+"/")
