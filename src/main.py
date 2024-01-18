import logging
from domain.logger import new_colored_logger


def start():
    """Start services."""
    logger = new_colored_logger('main', level=logging.DEBUG)
    logger.info('info')
    logger.debug('debug')
    logger.warning('warning')
    logger.fatal('fatal')
    

if __name__ == '__main__':
    start()
    