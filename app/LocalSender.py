import json
import hashlib
import os
import uuid

import requests

from app.ContentSender import ContentSender


class LocalSender(ContentSender):

    def __init__(self, token, namespace, format):
        super().__init__(token, namespace, format)

    def send(self, title, body):
        with open(self.namespace + title + ".txt", "w", encoding="utf-8") as f:
            f.write(body)
