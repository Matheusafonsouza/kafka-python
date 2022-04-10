from common.logger import log
from sys import exit

def process():
    pass

if __name__ == "__main__":
    log.info("Starting publisher service.")
    
    try:
        while True:
            process()
    except Exception:
        pass
    finally:
        log.info("Stoping publisher service.")
        exit()