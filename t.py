from abc import ABC, abstractmethod
class Vehicle(ABC):
   #@abstractmethod
   def drive(self):
    print("Vehicle is driving")
    #pass
 
    def new_fn(self):
        print("My new fn")

class Car(Vehicle):
    pass
    #def drive(self):
    #def return "Car is driving"

# Example 6: Using abstraction


car = Car()
print(car.drive())  # Output: Car is driving

# veh = Vehicle()
#print(veh.drive())  # Access abstract method