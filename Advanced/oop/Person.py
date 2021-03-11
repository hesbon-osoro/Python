#Person class: GoalKicker.com – Python® Notes for Professionals
class Person(object):
    'A simple class' #docstring
    species = 'Homo Sapiens' #class attribute
    def __init__(self,name): #special method
        "This is the initializer. It's a special method (see below)"
        self.name = name
    def __str__(self): #special method
        """This method is run when Python tries to cast the object to a string.
        Return this string when using print(). etc"""
        return self.name #instance attribute
    def rename(self,renamed): #regular method
        "Reassign and print the name attribute"
        self.name = renamed
        print("Now my name is {}".format(self.name))

print("""class Person(object):
    'A simple class' #docstring
    species = 'Homo Sapiens' #class attribute
    def __init__(self,name): #special method
        "This is the initializer. It's a special method (see below)"
        self.name = name
    def __str__(self): #special method
        \"""This method is run when Python tries to cast the object to a string.
        Return this string when using print(). etc\"""
        return self.name #instance attribute
    def rename(self,renamed): #regular method
        "Reassign and print the name attribute"
        self.name = renamed
        print("Now my name is {}".format(self.name))
        
""")


print("""There are a few things to note when looking at the above example.
1. The class is made up of attributes (data) and methods (functions).
2. Attributes and methods are simply deﬁned as normal variables and functions.
3. As noted in the corresponding docstring, the __init__() method is called the initializer. It's equivalent to the3. constructor in other object oriented languages, and is the method that is ﬁrst run when you create a new object, or new instance of the class. 
4. Attributes that apply to the whole class are deﬁned ﬁrst, and are called class attributes.
5. Attributes that apply to a speciﬁc instance of a class (an object) are called instance attributes. They are generally deﬁned inside __init__(); this is not necessary, but it is recommended (since attributes deﬁned outside of __init__() run the risk of being accessed before they are deﬁned). 
6. Every method, included in the class deﬁnition passes the object in question as its ﬁrst parameter. The word self is used for this parameter (usage of self is actually by convention, as the word self has no inherent meaning in Python, but this is one of Python's most respected conventions, and you should always follow it).
7. Those used to object-oriented programming in other languages may be surprised by a few things. One is that Python has no real concept of private elements, so everything, by default, imitates the behavior of the C++/Java public keyword. For more information, see the "Private Class Members" example on this page. 
8. Some of the class's methods have the following form: __functionname__(self, other_stuff). All such8. methods are called "magic methods" and are an important part of classes in Python. For instance, operator overloading in Python is implemented with magic methods. For more information, see the relevant""")

#instances
kelly = Person("Kelly")
joseph = Person('Joseph')
john_doe = Person("John Doe")

print("""kelly = Person("Kelly")
joseph = Person('Joseph')
john_doe = Person("John Doe")\n""")
print("kelly:",kelly)
print("joseph:",joseph)
print("john_doe:",john_doe)
print("john_doe.rename('John')")
john_doe.rename('John')
