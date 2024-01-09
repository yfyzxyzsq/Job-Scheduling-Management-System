import logging

# 创建一个logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 设置日志级别为DEBUG，这样DEBUG及以上级别的日志都会被记录

# 创建一个handler，用于将日志输出到文件
file_handler = logging.FileHandler('my_log.log')
file_handler.setLevel(logging.DEBUG)

# 创建一个handler，用于将日志输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  # 设置控制台输出的日志级别为ERROR

# 创建一个formatter，用于设置日志的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 将formatter添加到handler中
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将handler添加到logger中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 测试日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

当你运行上述代码时，所有级别的日志都会被写入到名为my_log.log的文件中，但是只有ERROR和CRITICAL级别的日志会输出到控制台。这是因为我们为两个不同的handler设置了不同的日志级别。

文件my_log.log会在你运行脚本的同目录下生成。如果你想要将日志输出到其他位置，只需要在创建FileHandler时指定完整的文件路径即可。

此外，你还可以为日志添加时间戳、日志级别、日志发生的位置等信息，这些都可以通过修改Formatter来实现。在Formatter中，%(asctime)s、%(name)s、%(levelname)s和%(message)s分别代表了时间戳、logger的名字、日志级别和日志信息。你可以根据需要添加或删除这些组件来自定义日志的格式。