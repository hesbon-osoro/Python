#Object Oriented
print("***OBJECT ORIENTED***")
print("""Python has been an object-oriented language since the time it existed. Due to this, creating and using classes and objects are downright easy. This chapter helps you become an expert in using Python's object-oriented programming support. 
If you do not have any previous experience with object-oriented (OO) programming, you may want to consult an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts. 
However, here is a small introduction of Object-Oriented Programming (OOP) to help you. """)

print("\n*Overview of OOP Terminology*")
print("*Class: A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation. ")
print("*Class variable: A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are. ")
print("*Data member: A class variable or instance variable that holds data associated with a class and its objects. ")
print("*Function overloading: The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.")
print("*Instance variable: A variable that is defined inside a method and belongs only to the current instance of a class.")
print("*Inheritance: The transfer of the characteristics of a class to other classes that are derived from it. ")
print("*Instance: An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.")
print("*Instantiation: The creation of an instance of a class. ")
print("*Method: A special kind of function that is defined in a class definition.")
print("*Object: A unique instance of a data structure that is defined by its class. An object comprises both data members (class variables and instance variables) and methods. ")
print("*Operator overloading: The assignment of more than one function to a particular operator.")

print("\n*Creating Classes*")
print("""The class statement creates a new class definition. The name of the class immediately follows the keyword class followed by a colon as follows- 
class ClassName: 
   'Optional class documentation string' 
   class_suite 
    * The class has a documentation string, which can be accessed viaClassName.__doc__.  
    * The class_suite consists of all the component statements defining class members, data attributes and functions. """)

print("\nExample")

print("""class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employess %d"%Employee.empCount)
    def displayEmployee(self):
        print("Name: ",self.name,", Salary: ",self.salary)\n""")
class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employess %d"%Employee.empCount)
    def displayEmployee(self):
        print("Name: ",self.name,", Salary: ",self.salary)

print("""   * The variable empCount is a class variable whose value is shared among all the instances of a in this class. This can be accessed as Employee.empCount from inside the class or outside the class.  
    * The first method  __init__() is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.  
    *  You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.""")

print("\n*Creating Instance Objects*")
print("""To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts. """)
print("""\n#This would create first object of Employee class
emp1 = Employee("Grace",10000)
#This would create secod object of Employee class
emp2 = Employee("Leshan",8000)""")
#This would create first object of Employee class
emp1 = Employee("Grace",10000)
#This would create secod object of Employee class
emp2 = Employee("Leshan",8000)

print("\n*Accessing Attributes*")
print("""You access the object's attributes using the dot operator with object. Class variable would be accessed using class name as follows- """)

print("""emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: %d"%Employee.empCount)\n""")
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee: %d"%Employee.empCount)

print("""\nYou can add, remove, or modify attributes of classes and objects at any time- 
emp3 = Employee("",0)
emp3.name = 'Lynne'
emp3.salary = 7500\n""")
emp3 = Employee("",0)
emp3.name = 'Lynne'
emp3.salary = 7500

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee: %d"%Employee.empCount)

print("""\nInstead of using the normal statements to access attributes, you can use the following functions- 
    * The getattr(obj, name[, default]): to access the attribute of object.  
    * The hasattr(obj,name): to check if an attribute exists or not.  
    * The setattr(obj,name,value): to set an attribute. If attribute does not exist, then it would be created.  
    * The delattr(obj, name): to delete an attribute. \n""")

print("""print("hasattr(emp1,'name'):",hasattr(emp1,'name'))
print("hasattr(emp1,'age'):",hasattr(emp1,'age'))
print("getattr(emp1,'name'):",getattr(emp1,'name'))
print("delattr(emp3,'salary'):",delattr(emp3,'salary'))
print("setattr(emp3,'salary',6000):",setattr(emp3,'salary',6000))""")
print("hasattr(emp1,'name'):",hasattr(emp1,'name'))
print("hasattr(emp1,'age'):",hasattr(emp1,'age'))
print("getattr(emp1,'name'):",getattr(emp1,'name'))
print("delattr(emp3,'salary'):",delattr(emp3,'salary'))

#print("emp3.salary:",emp3.salary)
#You can't access the attribute after it is deleted, it raises AttributeError
#AttributeError: 'Employee' object has no attribute 'salary'
print("setattr(emp3,'salary',6000):",setattr(emp3,'salary',6000))

print("\n*Built-In Class Attributes*")
print("""Every Python class keeps the following built-in attributes and they can be accessed using dot operator like any other attribute − 
    * __dict__: Dictionary containing the class's namespace. 
    * __doc__: Class documentation string or none, if undefined. 
    * __name__: Class name. 
    * __module__: Module name in which the class is defined. This attribute is "__main__" in interactive mode.
    * __bases__: A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list. \n""")

print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)

print("\n*Destroying Objects (Garbage Collection)*")
print("""Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically reclaims blocks of memory that no longer are in use is termed as Garbage Collection. 
Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes. 
An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it is deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically. 
a = 40      # Create object <40> 
b = a       # Increase ref. count  of <40>  
c = [b]     # Increase ref. count  of <40>   
del a       # Decrease ref. count  of <40> 
b = 100     # Decrease ref. count  of <40>  
c[0] = -1   # Decrease ref. count  of <40>  
You normally will not notice when the garbage collector destroys an orphaned instance and reclaims its space. However, a class can implement the special method__del__(), called a destructor, that is invoked when the instance is about to be destroyed. This method might be used to clean up any non-memory resources used by an instance. """)


print("\nExample")
print("""This __del__() destructor prints the class name of an instance that is about to be destroyed.""")
print("""class Point:
    def __init(self, x=0, y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1\n""")
class Point:
    def __init(self, x=0, y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1

#print the ids of the objects
print("id(pt1),id(pt2),id(pt3):",id(pt1),id(pt2),id(pt3))
print("""del pt1
del pt2
del pt3""")
del pt1
del pt2
del pt3

print("""\n*Note: Ideally, you should define your classes in a separate file, then you should import them in your main program file using import statement. 
In the above example, assuming definition of a Point class is contained in point.py and there is no other executable code in it. """)

print("\n*Class Inheritance*")
print("""Instead of starting from a scratch, you can create a class by deriving it from a pre-existing class by listing the parent class in parentheses after the new class name. 
The child class inherits the attributes of its parent class, and you can use those attributes as if they were defined in the child class. A child class can also override data members and methods from the parent. 

Syntax 
Derived classes are declared much like their parent class; however, a list of base classes to inherit from is given after the class name − 
class SubClassName (ParentClass1[, ParentClass2, ...]): 
   'Optional class documentation string' 
   class_suite """)

print('\nExample')
print("""class Parent: #define parent class
    parentAttr = 100
    def __init__(self):
        print("Calling the parent constructor")
    def parentMethod(self):
        print("Calling the parent method")
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attribute:",Parent.parentAttr)
class Child(Parent): #define child class
    def __init__(self):
        print("Calling child constructor")
    def childMethod(self):
        print("Calling child method")\n""")
class Parent: #define parent class
    parentAttr = 100
    def __init__(self):
        print("Calling the parent constructor")
    def parentMethod(self):
        print("Calling the parent method")
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("Parent attribute:",Parent.parentAttr)
class Child(Parent): #define child class
    def __init__(self):
        print("Calling child constructor")
    def childMethod(self):
        print("Calling child method")
print("""c = Child() 
c.childMethod() 
c.parentMethod() 
c.setAttr(200) 
c.getAttr() 
""")
c = Child() #instance of child
c.childMethod() #child calls its method
c.parentMethod() #calls parent's method
c.setAttr(200) #again call parent's method
c.getAttr() #again call parent's method

print("""In a similar way, you can drive a class from multiple parent classes as follows- 
class A:        # define your class A 
..... 
class B:         # define your calss B 
..... 
class C(A, B):   # subclass of A and B 
.....
You can use issubclass() or isinstance() functions to check a relationship of two classes and instances. 
    * The issubclass(sub, sup) boolean function returns True, if the given subclass sub is indeed a subclass of the superclass sup.  
    * The isinstance(obj, Class) boolean function returns True, if obj is an instance of class Class or is an instance of a subclass of Class. \n""")
print("issubclass(Parent,Child):",issubclass(Parent,Child))
print("issubclass(Child,Parent):",issubclass(Child,Parent))
print("isinstance(emp1,Employee):",isinstance(emp1,Employee))
print("\n*Overriding Methods*")
print("""You can always override your parent class methods. One reason for overriding parent's methods is that you may want special or different functionality in your subclass. """)
print("""class Parent1:
    def myMethod(self):
        print("Calling parent method")
class Child1(Parent1):
    def myMethod(self):
        print("Calling child method")""")
class Parent1:
    def myMethod(self):
        print("Calling parent method")
class Child1(Parent1):
    def myMethod(self):
        print("Calling child method")

print("""\nc =Child1() #instance of child
c.myMethod() #child calls overridden method""")
c =Child1() #instance of child
c.myMethod() #child calls overridden method

print('\n*Base Overloading Methods*')
print("""The following table lists some generic functionality that you can override in your own classes- """)
print("\nSN\tMethod, Description & Sample Call")
print("1\t__init__ ( self [,args...] ) Constructor (with any optional arguments) Sample Call : obj = className(args)")
print("2\t__del__( self ) Destructor, deletes an object Sample Call : del obj ")
print("3\t__repr__( self ) Evaluatable string representation Sample Call : repr(obj)")
print("4\t__str__( self ) Printable string representation Sample Call : str(obj) ")
print("5\t__cmp__ ( self, x ) Object comparison Sample Call : cmp(obj, x) ")

print("\n*Overloading Operators*")
print("""Suppose you have created a Vector class to represent two-dimensional vectors. What happens when you use the plus operator to add them? Most likely Python will yell at you. 
You could, however, define the __add__ method in your class to perform vector addition and then the plus operator would behave as per expectation − """)

print("""class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)'%(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)\n""")
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)'%(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a, self.b+other.b)
print("""v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1+v2)\n""")
v1 = Vector(2,10)
v2 = Vector(5,-2)
print("v1",v1+v2)


print('\n*Data Hiding*')
print("""An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then will not be directly visible to outsiders. """)

print('\nExample')
print("""class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount +=1
        print(self.__secretCount)""")
class JustCounter:
    __secretCount = 0
    def count(self):
        self.__secretCount +=1
        print(self.__secretCount)

print("""\ncounter = JustCounter()
counter.count()
counter.count()
counter.count()""")
counter = JustCounter()
counter.count()
counter.count()
counter.count()
#print (counter.__secretCount)
#AttributeError: 'JustCounter' object has no attribute '__secretCount'

print("""\nPython protects those members by internally changing the name to include the class name. You can access such attributes as object._className__attrName. If you would replace your last line as following, then it works for you- 
......................... 
print (counter._JustCounter__secretCount)""")