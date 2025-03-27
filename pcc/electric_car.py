"""A set of classes that can be used to represent electric car."""

from car import Car
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """Initialise attributes of the parent class."""
        super().__init__(make,model,year)
#         self.battery_size=40
        self.battery = Battery()
        
    def desc_battery(self):
        """Print battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    

class Battery():
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")
    def get_range(self):
        """Print's the range of the battery."""
        if self.battery_size==40:
            range = 150
        elif self.battery_size==65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")