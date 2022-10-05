# Create a class vehicle with acceleration and mileage attribute

class Vehicle:
    def __init__(self, speed_in_kph: float, fuel_in_litres: float) -> None:
        self.speed_in_kph = speed_in_kph # initial velocity
        self.fuel_in_litres = fuel_in_litres # Fuel available
        
    def acceleration(self, current_speed: float, time_elapsed_in_hr: float) -> float:
        # the acceleration is given in m/s^2
        acceleration = ((current_speed - self.speed_in_kph)/ time_elapsed_in_hr)*(5/18)
        return f"\nyour acceleration is {round(acceleration, 2)}m/s^2"
    
    def mileage(self) -> float:
        # taking 1l of fuel goes 12.5km
        mileage = self.fuel_in_litres * 3.0
        return f"\n{mileage}km to refueling\n"
     
# 1st instance of class vehicle   
toyota = Vehicle(0, 20)
print(toyota.acceleration(80, 3))
print(toyota.mileage())

# 2nd instance of class vehicle
vits = Vehicle(10, 30)
print(vits.acceleration(100, 5))
print(vits.mileage())
