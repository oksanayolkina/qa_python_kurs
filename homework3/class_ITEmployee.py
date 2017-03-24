from lesson3.test5 import Employee

class ITEmployee(Employee):

    def __init__(self, name=None, surname=None, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self.skill = []
        self.skills = []

    def add_skill(self, new_skill):
        self.skill.append(new_skill)

    def add_skills(self, new_skill1, new_skill2, new_skill3):
        self.skills.append(new_skill1)
        self.skills.append(new_skill2)
        self.skills.append(new_skill3)


if __name__ == "__main__":
    d = ITEmployee("Masha", "Ivanova", "QA")
    #print(d.full_name(), d.position)

    d.add_skill("qa automation")
    d.add_skill("git")
    d.add_skill("PyCharm")
    print(d.full_name(), d.position, d.skills)

    b = ITEmployee("Masha", "Ivanova", "QA")
    b.add_skills("qa automation1", "qa automation2", "qa automation3")
    print(b.skills)