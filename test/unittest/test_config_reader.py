import unittest

from app.ConfigReader import ConfigReader


class ConfigReaderTest(unittest.TestCase):
    def test_should_return_config_info(self):
        config = ConfigReader("../../config.json").read_auth()
        self.assertEqual(config.appid, "fb0d46b1")
        self.assertEqual(config.secret_key, "28d4a3f53e3a0386ecb941522f1335c8")
        self.assertEqual(config.token, "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP")
        self.assertEqual(config.namespace, "baili-qq4sf/bgzr5s")
        self.assertEqual(config.format, "html")
        self.assertEqual(config.file_path, "D:/ylliu/tz/record/")
