from lesson3.test5 import Employee

class ITEmployee(Employee):
    def __init__(self, name=None, surname=None, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self.skills = []
    def add_skills(self, new_skill):
        self.skills.append(new_skill)


if __name__ == "__main__":
    d = ITEmployee("Masha", "Ivanova", "QA")
    #print(d.full_name(), d.position)

    d.add_skills("qa automation")
    d.add_skills("git")
    d.add_skills("PyCharm")
    print(d.full_name(), d.position, d.skills)