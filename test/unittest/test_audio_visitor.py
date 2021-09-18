import os
import shutil
import unittest

from app.AudioVisitor import AudioVisitor
from app.ConfigReader import ConfigReader


class AudioVisitorTest(unittest.TestCase):
    def setUp(self):
        self.config = ConfigReader("../../config.json").read_auth()

    def test_get_supported_audio_files_from_path(self):
        case_dir = "../test_audio/"
        files_to_be_copied = [case_dir + "1.mp3",
                              case_dir + "3.m4a",
                              case_dir + "9-12-中文名字.mp3",
                              case_dir + "9.mp3"]
        for file in files_to_be_copied:
            shutil.copy(file, self.config.file_path)
        files_expected = [self.config.file_path + "1.mp3",
                          self.config.file_path + "3.m4a",
                          self.config.file_path + "9-12-中文名字.mp3",
                          self.config.file_path + "9.mp3"]

        files = AudioVisitor(self.config.file_path).get_supported_audio_files()
        self.assertCountEqual(files_expected, files)
        for file in files:
            os.remove(file)
