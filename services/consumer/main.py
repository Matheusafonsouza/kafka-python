from common.logger import log
from sys import exit

def process():
    pass

if __name__ == "__main__":
    log.info("Starting consumer service.")
    
    try:
        while True:
            process()
    except Exception:
        pass
    finally:
        log.info("Stoping consumer service.")
        exit()