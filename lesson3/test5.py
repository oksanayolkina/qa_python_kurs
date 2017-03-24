class Employee:
    title = "Infopuls"
    def __init__(self, name, surname, position = None):
        self.name = name
        self.surname = surname
        self.position = position
    def set_name(self, name):
        self.name = name
    def set_surname(self, surname):
        self.surname = surname
    def set_position (self, position):
        self.position = position
    def full_name(self):
        result = self.name + ' ' + self.surname
        return result

if __name__ == "__main__":
    print("ha-ha-ha")