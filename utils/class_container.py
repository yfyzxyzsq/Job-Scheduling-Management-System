class Registry:
    def __init__(self):
        self.classes = {}

    def add_class(self, cls):
        self.classes[str(cls)] = cls
        
    def get_classes(self, class_name):
        return self.classes[class_name]

