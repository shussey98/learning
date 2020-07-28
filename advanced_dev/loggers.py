import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('test_logger')

logger.info('This will not show')
logger.warning('This will show')

"""
DEBUG
INFO
WARNING
ERROR
CRitICAL

"""