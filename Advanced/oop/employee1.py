from person1 import Person

class Employee(Person):
    def __init__(self, first_name, last_name, age, job_title, salary):
        super().__init__(first_name, last_name, age)

        self.job_title = job_title
        self.salary = salary

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, value):
        self.__job_title = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Salary must be greater than zero')

        self.__salary = value

    def introduce(self):
        introduction = super().introduce()
        introduction += f" I'm a {self.job_title}"
        return introduction