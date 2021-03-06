
import logging


# create logger
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create file handler and set level to warning
fh = logging.FileHandler('mylog.log')
fh.setLevel(logging.WARNING)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

