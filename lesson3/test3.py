class Employee:
    title = "Infopuls"
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def set_name(self, name):
        self.name = name
    def set_position (self, position):
        self.position = position