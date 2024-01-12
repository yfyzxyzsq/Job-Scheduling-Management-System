from command.command_parser import CommandParser 
from utils.class_container import Registry
class CLI:
    def __init__(self, registry):
        self.registry = registry
        self.command_parser = CommandParser()

    def start(self):
        # 启动CLI，等待用户输入命令
        print(f'system starting ...')
        while True:
            command_input = input(">")
            self.command_parser.parse_execute(command_input)