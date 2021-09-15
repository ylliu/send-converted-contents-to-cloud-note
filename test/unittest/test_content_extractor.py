import unittest

from app.ContentExtractor import ContentExtractor


class ContentExtractorTest(unittest.TestCase):
    def test_should_extract_content_from_convert_result(self):
        content_expected = "大家好，我是某某某，今天由我跟大家"
        json_convert_result = '[{\"bg\":\"610\",\"ed\":\"7580\",\"onebest\":\"大家好，\",\"speaker\":\"0\"},' \
                         '{\"bg\":\"7580\",\"ed\":\"15400\",\"onebest\":\"我是某某某，今天由我跟大家\",\"speaker\":\"0\"}]'

        self.content_extractor = ContentExtractor(json_convert_result)
        self.assertEqual(content_expected,self.content_extractor.extract())

