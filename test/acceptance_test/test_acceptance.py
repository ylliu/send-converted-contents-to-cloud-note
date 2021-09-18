import hashlib
import json
import os
import shutil
import unittest

import requests

from app.ConfigReader import ConfigReader
from app.XunFeiConvertor import XunFeiConvertor
# 验收条件就是构造各种配置参数看是否可以通过
from main import convert_record_and_send_out


def copy_test_audio_file_to(dist_path):
    files_to_be_copied = "../test_audio/3.m4a"
    shutil.copy(files_to_be_copied, dist_path)


def create_json_config(file_path, save_type):
    config = {
        "appid": "fb0d46b1",
        "secret_key": "28d4a3f53e3a0386ecb941522f1335c8",
        "file_path": file_path,
        "save_type": save_type,
        "token": "WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP",
        "namespace": "baili-qq4sf/bpg3xc",
        "format": "html",
    }
    with open("../../config_test.json", "w", encoding="utf-8") as f:
        json.dump(config, f)


class AcceptanceTest(unittest.TestCase):

    def setUp(self):
        self.expected_content = '喂喂喂喂喂喂喂喂。'
        self.config_file_path = "D:/ylliu/tz/record/"
        self.default_file_path = os.getcwd() + "/"
        self.json_path = "../../config_test.json"
        self.YUQUE = "yuque"
        self.LOCAL = "local"

    def test_save_converted_content_to_local_txt_use_default_file_path(self):
        # given
        create_json_config("", self.LOCAL)
        copy_test_audio_file_to(self.default_file_path)
        # when
        convert_record_and_send_out(self.json_path)
        # then
        self.assertLocalTxtResult(self.default_file_path)

    def test_save_converted_content_to_local_txt_use_config_file_path(self):
        # given
        create_json_config(self.config_file_path, self.LOCAL)
        copy_test_audio_file_to(self.config_file_path)
        # when
        convert_record_and_send_out(self.json_path)
        # then
        self.assertLocalTxtResult(self.config_file_path)

    def assertLocalTxtResult(self, file_path):
        created_file = file_path + "3.txt"
        self.assertTrue(os.path.exists(created_file))
        with open(created_file, "r", encoding="utf-8") as f:
            content = f.readlines()
        self.assertEqual([self.expected_content], content)
        os.remove(created_file)

    def test_save_converted_content_to_yuque_note_use_default_file_path(self):
        # given

        create_json_config("", self.YUQUE)
        copy_test_audio_file_to(self.default_file_path)
        # when
        convert_record_and_send_out(self.json_path)
        # then
        self.assertYuQueResult()

    def test_save_converted_content_to_yuque_note_use_config_file_path(self):
        # given
        create_json_config(self.config_file_path, self.YUQUE)
        copy_test_audio_file_to(self.config_file_path)
        # when
        convert_record_and_send_out(self.json_path)
        # then
        self.assertYuQueResult()

    def assertYuQueResult(self):
        # 调用语雀的接口获取文章的内容
        headers = {
            'X-Auth-Token': 'WkXkkjiHp6JHy8Xj2GrHKoA8j24be9cvFBYOOQLP'
        }
        title = "3"
        slug = hashlib.md5(title.encode(encoding='UTF-8')).hexdigest()
        doc_details = requests.get('https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + slug,
                                   headers=headers)
        json_response = json.loads(doc_details.text)

        self.assertEqual(self.expected_content, json_response["data"]["body"])
        self.assertEqual('3', json_response["data"]["title"])
        article_id = json_response["data"]["id"]
        delete_response = requests.delete(
            'https://www.yuque.com/api/v2/repos/baili-qq4sf/bpg3xc/docs/' + str(article_id),
            headers=headers)
        self.assertEqual(200, delete_response.status_code)
