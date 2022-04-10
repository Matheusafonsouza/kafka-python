import logging
import sys
from os import getenv

from common.enums import Env

# SERVICE ENV
ENVIRONMENT = getenv('ENVIRONMENT', Env.DEVELOPMENT.value)

# set logging level
LOG_LEVEL = logging.INFO
if ENVIRONMENT == 'DEVELOPMENT':
    LOG_LEVEL = logging.DEBUG

# init logger
log = logging.getLogger(__name__)
log.setLevel(LOG_LEVEL)

# sets log format
LOG_FORMAT = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d}' + \
    '%(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT, '%m-%d %H:%M:%S')

# stdout log configuration
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(LOG_LEVEL)

# add handlers to logger
log.addHandler(consoleHandler)