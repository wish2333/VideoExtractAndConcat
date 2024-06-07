import logging
import logging.handlers
import os

# 日志配置
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if not os.path.exists(r'log'):
    os.mkdir(r'log')

file_handler = logging.handlers.RotatingFileHandler(r'log/log.txt', mode='a', encoding='utf-8', maxBytes=1024 * 1024 * 5, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s-%(name)s-%(levelname)s - %(message)s'))

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('\n')