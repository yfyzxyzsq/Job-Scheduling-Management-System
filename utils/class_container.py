
class Registry:
    def __init__(self, logger):
        self.log_flag = f'[Registry]'
        self.resources = {}
        self.logger = logger
        

    def add_class(self, name, obj):
        # print(f'add_class: {str(cls)}')
        self.logger.info(f'{self.log_flag} add {name} to registry')
        self.resources[name] = obj
        
    def get_class(self, name):
        return self.resources[name]

