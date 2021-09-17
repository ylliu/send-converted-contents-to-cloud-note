import json
import os

from app.Config import Config
from app.ContentExtractor import ContentExtractor
from app.TextOptimizer import TextOptimizer


class RecordConvertService(object):
    def __init__(self, record_convertor, content_sender, file_path):
        self.record_convertor = record_convertor
        self.content_sender = content_sender
        self.file_path = file_path

    def get_supported_audio_files_from(self):
        result = []
        format_supported = ["wav", "flac", "opus", "m4a", "mp3"]
        files = os.listdir(self.file_path)
        for file in files:
            if file.split(".")[1] not in format_supported:
                continue
            result.append(os.path.join(self.file_path, file))
        if len(result) == 0:
            print("请检查" + self.file_path + "下是否放置了音频文件")
        return result

    def extract_file_name_form(self, file_path):
        str_list = file_path.split('.')
        file_name = str_list[0]
        name_list = file_name.split("/")
        return name_list[len(name_list) - 1]

    def convert(self, path):
        converted_data = self.record_convertor.convert(path)
        extracted_content = ContentExtractor(converted_data).extract()
        optimized_content = TextOptimizer(extracted_content).optimize()
        title = self.extract_file_name_form(path)
        return self.content_sender.send(title, optimized_content)

    def read_auth(self, config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
        return Config(json_data["appid"],
                      json_data["secret_key"],
                      json_data["token"],
                      json_data["namespace"],
                      json_data["format"])

    def send_converted_contents_to_cloud_note(self):
        file_paths = self.get_supported_audio_files_from()
        for file_path in file_paths:
            self.convert(file_path)
            # 删除文件，防止出现忘记删除文件，导致重新识别浪费转写服务时长
            os.remove(file_path)
