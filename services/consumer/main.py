from sys import exit

from adapters.kafka.services import Consumer
from common.logger import log


def callback(message):
    msg = (
        f"{message.topic}:{message.partition}:{message.offset}: "
        f"{message.key=} {message.value=}"
    )
    log.info(msg)


if __name__ == "__main__":
    log.info("Starting consumer service.")
    
    try:
        Consumer(topics=["test-topic"], callback=callback).start()
    except Exception as exception:
        log.exception(exception)
        log.info("Stoping consumer service.")
        exit()