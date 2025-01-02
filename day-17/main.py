class Car:

    def __init__(self, seats,model):
        self.seats = seats
        self.model = model
        self.milage = 0

    def dist(self, rounds):
        self.milage += (rounds*100)



my_car = Car(5, "BMW")
his_car = Car(7, "Audi")
my_car.dist(4)
print(my_car.seats, my_car.model, my_car.milage)
print(his_car.seats, his_car.model, his_car.milage)
