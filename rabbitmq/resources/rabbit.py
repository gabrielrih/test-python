# Reference: https://pypi.org/project/pika/
import pika

from resources.rabbit_cfg import RabbitCfg
from resources.enum.exchange_type import ExchangeType


class Rabbit():
    def __init__(self):
        rabbit_cfg = RabbitCfg()
        self._connection = self.open_connection(rabbit_cfg)

    def open_connection(self, rabbit_cfg):
        try:
            credentials = pika.PlainCredentials(rabbit_cfg.username, rabbit_cfg.password)
            parameters = pika.ConnectionParameters(host=rabbit_cfg.host, virtual_host=rabbit_cfg.virtual_host, credentials=credentials)
            connection = pika.BlockingConnection(parameters)
            return connection
        except pika.exceptions.ProbableAuthenticationError as exc:
            raise exc

    def open_channel(self):
        channel = self._connection.channel()
        return channel

    def close_channel(self, channel):
        channel.close()

    # Cancel channel and return any requeued_messages
    def cancel_channel(self, channel) -> int:
        return channel.cancel()

    def create_exchange(self, 
                        channel,
                        name:str,
                        exchange_type:ExchangeType=ExchangeType.Direct,
                        durable:bool=True,
                        auto_delete:bool=False,
                        internal:bool=False):
        try:
            channel.exchange_declare(name, exchange_type=exchange_type.value, durable=durable, auto_delete=auto_delete, internal=internal)
        except pika.exceptions.ChannelClosedByBroker as exc:
            raise exc

    def create_queue(self, channel, name:str, durable:bool=True, auto_delete:bool=False):
        try:
            channel.queue_declare(queue=name,durable=durable, auto_delete=auto_delete)
        except Exception as exc:
            raise exc

    def bind_queue(self, channel, exchange_name:str, queue_name:str, routing_key:str):
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    def send_message(self, channel, exchange_name:str, routing_key:str, message:str='Sample message'):
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

    def ack_message(self, channel, delivery_tag:int):
        channel.basic_ack(delivery_tag=delivery_tag)