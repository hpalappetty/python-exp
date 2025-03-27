"""A class that can be used as Car."""
class Car:
    """A simple attempy to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # adding a default value to an attribute.
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year}-{self.make}-{self.model}"
        return long_name.title()
    
    def get_odoreading(self):
        """Print a statement showing the new car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
        """
        Set the odo reading to given value. 
        Add a check to stop odo meter rollback in garages.    
        """
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Don't mess with the car! You can't tamper the Odo dude!")
    
    def increment_odometer(self, miles):
        """Mile crunching starts!"""
        self.odometer_reading+=miles

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