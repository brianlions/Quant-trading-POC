#!/usr/bin/env python3
import logging

_name2key = {
    'debug':    logging.DEBUG,
    'info':     logging.INFO,
    'warning':  logging.WARNING,
    'error':    logging.ERROR,
    'critical': logging.CRITICAL,
    }

def setup(level='info',
          msg_format='[%(asctime)s] [%(levelname)s]\t[%(filename)s:%(lineno)s:%(funcName)s] %(message)s'):
    if level not in _name2key:
        raise Exception('invalid logging level: {}'.format(str(level)))
    logging.basicConfig(format=msg_format, level=_name2key[level])

def reset_level(level='info'):
    if level not in _name2key:
        raise Exception('invalid logging level: {}'.format(str(level)))
    logging.warning('change logging level to: {}'.format(level))
    logging.getLogger().setLevel(_name2key[level])

#------------------------------------------------------------------------------

if __name__ == '__main__':
    def log_all():
        logging.debug('debug message')
        logging.info('info message')
        logging.warning('warning message')
        logging.error('error message')
        logging.critical('critical message')

    setup()
    log_all()
    reset_level('error')
    log_all()
