from command.command_parser import CommandParser 
from utils.class_container import Registry
class CLI:
    def __init__(self, registry:Registry):
        self.log_flag = f'[CLI]'
        self.logger = registry.get_class('logger')
        self.logger.info(f'{self.log_flag} init CLI')
        self.logger.info(f'{self.log_flag} init CLI')
        self.command_parser = registry.get_class('command_parser')
        
        

    def start(self):
        # 启动CLI，等待用户输入命令
        print(f'system starting ...')
        while True:
            command_input = input(">")
            self.command_parser.parse_execute(command_input)