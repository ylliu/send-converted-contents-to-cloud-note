import hashlib
import json
import os
import shutil
import unittest

import requests

from app.ConfigReader import ConfigReader
from app.XunFeiConvertor import XunFeiConvertor
# 验收条件就是构造各种配置参数看是否可以通过
from main import convert_record_and_send_to_cloud_app


class AcceptanceTest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()
        self.record_convertor = XunFeiConvertor(self.config.appid, self.config.secret_key)
        self.test_file = "D:/ylliu/tz/record_for_test/3.m4a"
        self.body = "喂喂喂喂喂喂喂喂。"

    def test_save_converted_content_to_local_txt_use_default_file_path(self):
        # configure a json file
        config = {
            "appid": "fb0d46b1",
            "secret_key": "28d4a3f53e3a0386ecb941522f1335c8",
            "token": "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP",
            "namespace": "baili-qq4sf/bgzr5s",
            "format": "html",
            "file_path": "",
            "save_type": "local"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        # copy a file to the run path
        case_dir = "D:/ylliu/tz/record_base_file/"
        files_to_be_copied = case_dir + "3.m4a"
        shutil.copy(files_to_be_copied, os.getcwd())

        convert_record_and_send_to_cloud_app("../../config_test.json")

        self.assertTrue(os.path.exists(self.config.file_path + "3.txt"))
        with open(self.config.file_path + "3.txt", "r", encoding="utf-8") as f:
            content = f.readlines()

        self.assertEqual(['喂喂喂喂喂喂喂喂。'], content)

        os.remove(self.config.file_path + "3.txt")

    def test_save_converted_content_to_local_txt_use_config_file_path(self):
        # configure a json file
        config = {
            "appid": "fb0d46b1",
            "secret_key": "28d4a3f53e3a0386ecb941522f1335c8",
            "token": "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP",
            "namespace": "baili-qq4sf/bgzr5s",
            "format": "html",
            "file_path": "D:/ylliu/tz/record/",
            "save_type": "local"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        # copy a file to the run path
        case_dir = "D:/ylliu/tz/record_base_file/"
        files_to_be_copied = case_dir + "3.m4a"
        shutil.copy(files_to_be_copied, "D:/ylliu/tz/record/")

        convert_record_and_send_to_cloud_app("../../config_test.json")

        self.assertTrue(os.path.exists(self.config.file_path + "3.txt"))
        with open(self.config.file_path + "3.txt", "r", encoding="utf-8") as f:
            content = f.readlines()

        self.assertEqual(['喂喂喂喂喂喂喂喂。'], content)
        os.remove(self.config.file_path + "3.txt")

    def test_save_converted_content_to_yuque_note_use_default_file_path(self):
        # configure a json file
        config = {
            "appid": "fb0d46b1",
            "secret_key": "28d4a3f53e3a0386ecb941522f1335c8",
            "token": "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP",
            "namespace": "baili-qq4sf/bpg3xc",
            "format": "html",
            "file_path": "",
            "save_type": "yuque"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        # copy a file to the run path
        case_dir = "D:/ylliu/tz/record_base_file/"
        files_to_be_copied = case_dir + "3.m4a"
        shutil.copy(files_to_be_copied, os.getcwd())

        convert_record_and_send_to_cloud_app("../../config_test.json")

        # 调用语雀的接口获取文章的内容
        headers = {
            'X-Auth-Token': 'WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP'
        }
        title = "3"
        slug = hashlib.md5(title.encode(encoding='UTF-8')).hexdigest()
        doc_details = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + slug,
                                   headers=headers)
        json_response = json.loads(doc_details.text)
        self.assertEqual('喂喂喂喂喂喂喂喂。', json_response["data"]["body"])
        self.assertEqual('3', json_response["data"]["title"])
        article_id = json_response["data"]["id"]
        delete_response = requests.delete(
            'https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + str(article_id),
            headers=headers)
        self.assertEqual(200, delete_response.status_code)

    def test_save_converted_content_to_yuque_note_use_config_file_path(self):
        # configure a json file
        config = {
            "appid": "fb0d46b1",
            "secret_key": "28d4a3f53e3a0386ecb941522f1335c8",
            "token": "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP",
            "namespace": "baili-qq4sf/bpg3xc",
            "format": "html",
            "file_path": "",
            "save_type": "yuque"
        }
        with open("../../config_test.json", "w", encoding="utf-8") as f:
            json.dump(config, f)
        # copy a file to the run path
        case_dir = "D:/ylliu/tz/record_base_file/"
        files_to_be_copied = case_dir + "3.m4a"
        shutil.copy(files_to_be_copied, os.getcwd())

        convert_record_and_send_to_cloud_app("../../config_test.json")

        # 调用语雀的接口获取文章的内容
        headers = {
            'X-Auth-Token': 'WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP'
        }
        title = "3"
        slug = hashlib.md5(title.encode(encoding='UTF-8')).hexdigest()
        doc_details = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + slug,
                                   headers=headers)
        json_response = json.loads(doc_details.text)
        print(json_response)
        self.assertEqual('喂喂喂喂喂喂喂喂。', json_response["data"]["body"])
        self.assertEqual('3', json_response["data"]["title"])
        article_id = json_response["data"]["id"]
        delete_response = requests.delete(
            'https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + str(article_id),
            headers=headers)
        self.assertEqual(200, delete_response.status_code)
