import os


class RabbitCfg():
    def __init__(self):
        super(RabbitCfg, self).__init__()
        self.host = os.getenv('RABBITMQ_HOST') or 'localhost'
        self.port = os.getenv('RABBITMQ_PORT') or 5672
        self.virtual_host = os.getenv('RABBITMQ_VHOST') or 'test'
        self.username = os.getenv('RABBITMQ_USERNAME')
        self.password = os.getenv('RABBITMQ_PASSWORD')
