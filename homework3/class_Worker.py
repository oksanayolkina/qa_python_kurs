class Worker:

    def __init__(self, full_name, position=None, salary=0, experience=0):
        self.full_name = full_name
        self.position = position
        self.salary = salary
        self.experience = experience

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_firstname(self):
        result = self.full_name.split(' ')
        return result[1]

    def get_lastname(self):
        result = self.full_name.split(' ')
        return result[0]

    def get_experience(self):
        if self.experience == 0:
            result = "Experience is absent"
        elif self.experience < 3:
            result = "Your level is JUNIOR"
        elif 3 <= self.experience <= 6:
            result = "Your level is MIDDLE"
        elif self.experience > 6:
            result = "Your level is SENIOR"
        return result

    def get_salary(self, qw):
        result = qw * self.salary
        return result