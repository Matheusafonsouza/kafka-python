from sys import exit

from adapters.kafka.services import Consumer
from adapters.event.schemas import Event
from common.logger import log


def callback(event: Event):
    msg = f"{event.event_id} - {event.timestamp}: {event.message}"
    log.info(msg)


if __name__ == "__main__":
    log.info("Starting consumer service.")
    
    try:
        Consumer(topics=["test-topic"], callback=callback).start()
    except Exception as exception:
        log.exception(exception)
        log.info("Stoping consumer service.")
        exit()