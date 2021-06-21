from argparse import ArgumentParser
import json

from fload import Source
from fload_freedb.freedb import FreedbClient, FreedbCollection


class FreedbSource(Source):
    freedb_url = None
    token = None
    db = None
    collection = None
    col: FreedbCollection = None
    query: str = None

    def start(self):
        params = {}
        if self.query:
            params['query'] = json.loads(self.query)
            
        for item in self.col.iter(**params):
            yield item

    def add_arguments(self, parser:ArgumentParser):
        parser.add_argument('--freedb-url', default='http://localhost:8000/')
        parser.add_argument('--token')
        parser.add_argument('--db')
        parser.add_argument('--collection')
        parser.add_argument('--query')
    
    def init(self, ops):
        self.freedb_url = ops.freedb_url
        self.token = ops.token
        self.db = ops.db
        self.collection = ops.collection
        self.query = ops.query

        client = FreedbClient(self.freedb_url, token=self.token)
        db = client.database(self.db)
        self.col = db.collection(self.collection)
    