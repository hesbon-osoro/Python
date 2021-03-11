class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f"Hi. I'm {self.full_name}. I'm {self.age} years old."
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('Age is not valid')

        self.__age = value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"