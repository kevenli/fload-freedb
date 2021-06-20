from argparse import ArgumentParser

from fload import Source
from fload_freedb.freedb import FreedbClient, FreedbCollection


class FreedbSource(Source):
    freedb_url = None
    token = None
    db = None
    collection = None
    col:FreedbCollection = None

    def start(self):
        for item in self.col.iter():
            yield item

    def add_arguments(self, parser:ArgumentParser):
        parser.add_argument('--freedb-url', default='http://localhost:8000/')
        parser.add_argument('--token')
        parser.add_argument('--db')
        parser.add_argument('--collection')
    
    def init(self, ops):
        self.freedb_url = ops.freedb_url
        self.token = ops.token
        self.db = ops.db
        self.collection = ops.collection

        client = FreedbClient(self.freedb_url, token=self.token)
        db = client.database(self.db)
        self.col = db.collection(self.collection)
    