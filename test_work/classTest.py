class Worker:

    def __init__(self, full_name, position=None, salary=None, experience=None):
        self.__full_name = full_name
        # self.position = position
        # self.salary = salary
        # self.experience = experience

    # def set_full_name(self, full_name):
    #     self.full_name = full_name
    #
    def get_firstname(self):
        result = self.__full_name.split(' ')
        return result[0]

    def get_lastname(self):
        result = self.__full_name.split(' ')
        return result[1]

    def set_lastname(self, lastname):
        self.__full_name = self.get_firstname() + ' ' + lastname

    def set_firstname(self, firstname):
        self.__full_name = firstname + ' ' + self.get_lastname()




            # def set_position(self, position):
    #      self.position = position

    # def surname(self, surname):
    #     self.surname = surname

    # def salary(self, salary, month=None):
    #     int(month)
    #     self.salary = salary * month
    #     print("Input the amount of months: ")
    #
    # def experience(self, experience):
    #     self.experience = experience
    #     if experience < (3 * 12):
    #         print("Your level is JUNIOR")
    #     elif (3 * 12) <= experience <= (6 * 12):
    #         print("Your level is MIDDLE")
    #     elif experience > (6 * 12):
    #         print("Your level is SENIOR")
