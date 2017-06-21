from gui.db.person import Person

class Manager(Person):
    def increaceSalary(self, percent, bonus=0.1):
        Person.increaceSalary(self, percent + bonus)
    # def __str__(self):
        # attrs = ''
        # for key in self.__dict__:
        #     attrs += '%s\\' % key
        # return attrs
    # def __add__(self):
       # print(self.getStatus())