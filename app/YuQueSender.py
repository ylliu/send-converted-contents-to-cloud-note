import json
import hashlib
import uuid

import requests

from app.ContentSender import ContentSender


class YuQueSender(ContentSender):

    def __init__(self, token, namespace,format):
        super().__init__(token, namespace,format)

    def send(self, title, body):
        headers = {
            'X-Auth-Token': self.token
        }
        data = {
            'Key': 'Description',
            'title': title,
            # the same title should not create again
            'slug': hashlib.md5(title.encode(encoding='UTF-8')).hexdigest(),
            'public': '0',
            'format': 'markdown',
            'body': body
        }
        create_doc = requests.post('https://www.yuque.com/api/v2/repos/' + self.namespace + '/docs', headers=headers,
                                   data=data)
        return create_doc.text
