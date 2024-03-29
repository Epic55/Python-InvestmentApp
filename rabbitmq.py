import pika, os, logging
CLOUD_AMQP = ''

def sendmsg():
    logging.basicConfig()

    url = os.environ.get('CLOUDAMQP_URL', f'{CLOUD_AMQP}')
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='MyQueue1')

    print("Preparing to send msg ...")
    channel.basic_publish(exchange='', routing_key='MyQueue1', body=input("Enter msg "))
    print("[x] Message sent to consumer")
    connection.close()
