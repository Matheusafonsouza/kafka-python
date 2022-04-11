#!/usr/bin/env python
import json
import threading, time
from typing import Callable

from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from common.logger import log


class Producer(threading.Thread):
    def __init__(self, topics: list[str] = None, event: dict = None):
        self.topics = topics
        self.event = event
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(
            api_version=(0, 10, 1),
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

        while not self.stop_event.is_set():
            for topic in self.topics:
                producer.send(topic, self.event)
            time.sleep(1)

        producer.close()


class Consumer(threading.Thread):
    def __init__(self, callback: Callable = None, topics: list[str] = None):
        self.callback = callback
        self.topics = topics
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(
            api_version=(0, 10, 1),
            bootstrap_servers='kafka:9092',
            auto_offset_reset='earliest',
            group_id='my-group',
            enable_auto_commit=True,
            consumer_timeout_ms=1000,
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )
        consumer.subscribe(self.topics)

        while not self.stop_event.is_set():
            for message in consumer:
                self.callback(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def create_topics():
    try:
        log
        admin = KafkaAdminClient(
            api_version=(0, 10, 1),
            bootstrap_servers='kafka:9092'
        )
        topic = NewTopic(name='test-topic',
                        num_partitions=1,
                        replication_factor=1)
        admin.create_topics([topic])
    except TopicAlreadyExistsError:
        pass