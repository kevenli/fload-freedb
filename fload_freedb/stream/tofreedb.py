from argparse import ArgumentParser
import re
import os

from fload import Pipeline
from fload_freedb.freedb import FreedbClient, FreedbCollection


class ToFreedb(Pipeline):
    freedb_url = None
    token = None
    db = None
    collection = None
    col:FreedbCollection = None
    exist_policy: str = 'skip'

    def add_arguments(self, parser:ArgumentParser):
        parser.add_argument('--freedb-url', default='http://localhost:8000/')
        parser.add_argument('--token')
        parser.add_argument('--db')
        parser.add_argument('--collection')
        parser.add_argument('--exist', choices=['skip', 'overwrite', 'merge'], default='skip')


    def init(self, ops):
        self.freedb_url = ops.freedb_url
        if ops.token:
            self.token = ops.token
        else:
            self.token = os.environ.get('FREEDB_TOKEN')
        self.db = ops.db
        self.collection = ops.collection
        self.exist_policy = ops.exist

        client = FreedbClient(self.freedb_url, token=self.token)
        db = client.database(self.db)
        self.col = db.collection(self.collection)

    def process(self, item):
        doc_id = item.get('id')
        if self.exist_policy == 'skip' or not doc_id:
            return self.col.post(item)
        elif self.exist_policy == 'replace':
            return self.col.put_doc(doc_id, item)
        elif self.exist_policy == 'merge':
            return self.col.merge_doc(doc_id, item)
