class Car:
    carCount = 0
    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.carCount += 1

    def displayCarCount(self):
        print("Total count of cars are %d" %Car.carCount)

    def showColorBrand(self):
        print("The color and Brand of the car is ",self.color, self.model)

car1 = Car("Red", "Ferrari")
car2 = Car("Black", "Lamborghini")

car1.showColorBrand()
car2.showColorBrand()
car2.displayCarCount()