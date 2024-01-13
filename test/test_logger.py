import logging
from datetime import datetime

if __name__ == '__main__':
    date = datetime.now()
    date = date.strftime(f'%Y%m%d')
    log_day = date
    log_path = f'/root/Job-Scheduling-Management-System/monitoring/log_file/{log_day}'
    logger = logging.getLogger('system_logger')
    logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG，这样DEBUG及以上级别的日志都会被记录
    # 创建一个handler，用于将日志输出到文件
    file_handler = logging.FileHandler(f'{log_path}/{log_day}.log')
    file_handler.setLevel(logging.DEBUG)
    # 创建一个handler，用于将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)  # 设置控制台输出的日志级别为ERROR
        
    # 创建一个formatter，用于设置日志的格式
    formatter = logging.Formatter('[%(pathname)s:%(lineno)d][%(asctime)s - %(name)s - %(levelname)s] %(message)s')

    # 将formatter添加到handler中
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 将handler添加到logger中
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.info('test----')
#     import logging

# # 创建一个日志记录器
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # 创建一个控制台日志处理器，并设置级别
# ch = logging.StreamHandler()

# # 创建日志格式器
# formatter = logging.Formatter('[%(pathname)s:%(lineno)d][%(asctime)s - %(name)s - %(levelname)s] %(message)s')

# # 添加格式器到处理器
# ch.setFormatter(formatter)

# # 添加处理器到日志记录器
# logger.addHandler(ch)

# # 记录一条消息
# logger.info('测试消息')