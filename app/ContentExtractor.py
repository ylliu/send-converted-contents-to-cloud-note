import json


class ContentExtractor(object):
    def __init__(self, json_convert_result):
        self.json_convert_result = json_convert_result

    def extract(self):
        result = ""
        json_data = json.loads(self.json_convert_result)
        for item in json_data:
            result += item["onebest"]
        return result
