import json

from app.Config import Config


class ConfigReader(object):
    def __init__(self, config_path):
        self.config_path = config_path

    def read_auth(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        return Config(json_data["appid"],
                      json_data["secret_key"],
                      json_data["token"],
                      json_data["namespace"],
                      json_data["format"],
                      json_data["file_path"],
                      json_data["save_type"])
