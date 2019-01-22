class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car' objects.")
        self.cars.append(car)

class Bird:
    def __init__(self, species):
        self.species = species

ford = Garage()
duck = Bird('Duck')

try:
    ford.add_car(duck)
except TypeError:
    print(f'Really? Do you trying add a bird into a garage, you dumbass motherfucker?')
except ValueError:
    print('Something weird happened...')