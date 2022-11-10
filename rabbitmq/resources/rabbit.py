# Reference: https://pypi.org/project/pika/
import pika

from resources.rabbit_cfg import RabbitCfg
from resources.enum.exchange_type import ExchangeType


class Rabbit():
    def __init__(self):
        rabbit_cfg = RabbitCfg()
        self._connection = self.__open_connection(rabbit_cfg)

    def __open_connection(self, rabbit_cfg):
        credentials = pika.PlainCredentials(rabbit_cfg.username, rabbit_cfg.password)
        parameters = pika.ConnectionParameters(host=rabbit_cfg.host, virtual_host=rabbit_cfg.virtual_host, credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        return connection

    def open_channel(self):
        channel = self._connection.channel()
        return channel

    def close_channel(self, channel):
        channel.close()

    def create_exchange(self, channel, name:str, durable:bool=True, exchange_type:ExchangeType=ExchangeType.Direct):
        channel.exchange_declare(name, durable=durable, exchange_type=exchange_type.value)

    def create_queue(self, channel, name:str, durable:bool=True, auto_delete:bool=False):
        channel.queue_declare(queue=name,durable=durable, auto_delete=auto_delete)

    def bind_queue(self, channel, exchange_name:str, queue_name:str, routing_key:str):
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    def send_message(self, channel, exchange_name:str, routing_key:str, message:str='Sample message'):
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

    def ack_message(self, channel, delivery_tag:int):
        channel.basic_ack(delivery_tag)