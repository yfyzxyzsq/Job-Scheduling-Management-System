# coding=utf-8
import logging
import os
from datetime import datetime


class Logger:
    
    def __init__(self):
        self.cur_abs_path = os.path.dirname(os.path.abspath(__file__))
        date = datetime.now()
        date = date.strftime(f'%Y%m%d')
        self.log_day = date
        self.log_path = f'{self.cur_abs_path}/log_file/{self.log_day}'
        os.makedirs(self.log_path, exist_ok=True)
        logger = logging.getLogger('system_logger')
        logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG，这样DEBUG及以上级别的日志都会被记录
        # 创建一个handler，用于将日志输出到文件
        file_handler = logging.FileHandler(f'{self.log_path}/{self.log_day}.log')
        file_handler.setLevel(logging.DEBUG)
        # 创建一个handler，用于将日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)  # 设置控制台输出的日志级别为ERROR
        
        # 创建一个formatter，用于设置日志的格式
        formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')

        # 将formatter添加到handler中
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 将handler添加到logger中
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        self.logger = logger
        self.logger.info(f'init logger ...')
        self.logger.info(f'running day: {self.log_day}, log level: {self.logger.level}')
        
        
        
    def LogDebug(self, message):
        self.logger.debug(message)
        
    
    def LogInfo(self, message):
        # 记录日志信息
        self.logger.info(message)
        
    def LogWarn(self, message):
        self.logger.warning(message)
    
    
    def LogError(self, message):
        self.logger.error(message)
        
    def LogCritical(self, message):
        self.logger.critical(message)
        
if __name__ == '__main__':
    logger = Logger()
    logger.LogDebug("debug")
    logger.LogInfo("info")
    logger.LogWarn("warn")
    logger.LogError("error")
    logger.LogCritical("critical")