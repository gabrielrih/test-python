from resources.rabbit import Rabbit
from resources.enum.exchange_type import ExchangeType

EXCHANGE_NAME="exchange-name"
EXCHANGE_TYPE=ExchangeType.Direct
QUEUE_NAME="queue-name"
ROUTING_KEY="queue-name"

def main():
    rabbit = Rabbit()
    channel = rabbit.open_channel()
    rabbit.create_exchange(channel=channel, name=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE)
    rabbit.create_queue(channel=channel, name=QUEUE_NAME, durable=False, auto_delete=False)
    rabbit.bind_queue(channel=channel, exchange_name=EXCHANGE_NAME, queue_name=QUEUE_NAME, routing_key=ROUTING_KEY)
    rabbit.send_message(channel=channel, exchange_name=EXCHANGE_NAME, routing_key=ROUTING_KEY)
    rabbit.close_channel(channel)

if __name__ == '__main__':
    main()