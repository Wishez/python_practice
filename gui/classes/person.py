class Person:
    def __init__(self, name, age, salary=0, job=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job
    def lastName(self):
        return self.name.split()[1]
    def firstName(self):
        return self.name.split()[0]
    def changeJob(self, newJob):
        self.job = newJob
    def addResponsibilities(self, additionalJob):
        self.job += ", %s" % additionalJob
    def increaceSalary(self, percent):
        self.salary *= (1.0 + percent)
    def reduceSalary(self, percent):
        self.salary /= (1.0 + percent)
    def changeAge(self, newAge):
        self.age = newAge
    def getStatus(self):
        return {
            'name': self.name,
            'age': self.age,
            'salary': self.salary,
            'job': self.job
        }
    def __str__(self):
        return '%s => %s' % (self.name, self.getStatus())