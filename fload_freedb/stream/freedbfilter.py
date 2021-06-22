import os

from fload import Pipeline

from fload_freedb.freedb import FreedbClient, FreedbCollection, DocumentDotExist

class FreedbDocNotExistFilter(Pipeline):
    freedb_url = None
    token = None
    db = None
    collection = None
    col:FreedbCollection = None

    def add_arguments(self, parser):
        parser.add_argument('--freedb-url', default='http://localhost:8000/')
        parser.add_argument('--token')
        parser.add_argument('--db')
        parser.add_argument('--collection')

    def init(self, ops):
        self.freedb_url = ops.freedb_url
        if ops.token:
            self.token = ops.token
        else:
            self.token = os.environ.get('FREEDB_TOKEN')
        self.db = ops.db
        self.collection = ops.collection

        client = FreedbClient(self.freedb_url, token=self.token)
        db = client.database(self.db)
        self.col = db.collection(self.collection)

    def process(self, item):
        id = item.get('id')
        if id is None:
            return item

        try:
            doc = self.col.doc(id)
            return None
        except DocumentDotExist:
            return item
