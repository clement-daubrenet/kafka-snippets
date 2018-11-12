from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(1000):
    producer.send('fast-messages', key=str.encode('key_{}'.format(i)),
                  value=b'some_message_bytes')
