class Decorator:
    def smart_divide(func):
        def inner(self, a, b):
            print("I am going to divide",a,"and",b)
            if b== 0:
                print("Whoops! cannot divide")
                return
            return func(self, a, b)
        return inner

    @smart_divide
    def divide(self, a, b):
        print(a/b)

obj = Decorator()
obj2 = Decorator()
obj.divide(4,0)
obj.divide(4,2)