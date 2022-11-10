from resources.rabbit import Rabbit

EXCHANGE_NAME="exchange-name"
QUEUE_NAME="queue-name"
ROUTING_KEY="queue-name"

def main():
    rabbit = Rabbit()
    channel = rabbit.open_channel()    

    # Get ten messages and break out
    for method_frame, properties, body in channel.consume(QUEUE_NAME):

        # Display the message parts
        print(method_frame)
        print(properties)
        print(body)

        # Acknowledge the message
        rabbit.ack_message(channel, method_frame.delivery_tag)

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == 10:
            break

    # Cancel the consumer and return any pending messages
    requeued_messages = rabbit.cancel_channel(channel)
    print('Requeued %i messages' % requeued_messages)

    # Close the channel and the connection
    rabbit.close_channel(channel)

if __name__ == '__main__':
    main()