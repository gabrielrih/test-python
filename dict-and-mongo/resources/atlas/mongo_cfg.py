import os


class MongoCfg():
    def __init__(self):
        super(MongoCfg, self).__init__()
        self.connection_string = os.getenv('MONGODB_ATLAS_CONNECTION_STRING')
        self.time_out_in_ms = os.getenv('MONGODB_ATLAS_TIME_OUT_IN_SEC') or 5000
        if not self.connection_string:
            raise 'Exception: var env MONGODB_ATLAS_CONNECTION_STRING was not found!'