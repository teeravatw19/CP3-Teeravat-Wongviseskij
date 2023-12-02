class Vehicle:
    licenseNumber = ""
    serialCode = ""
    def turnONair(self):
        print("Air Turn : ON")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.turnONair()

pickup1 = PickUp()
pickup1.turnONair()

van1 = Van()
van1.turnONair()

estatecar1 = Estatecar()
estatecar1.turnONair()
