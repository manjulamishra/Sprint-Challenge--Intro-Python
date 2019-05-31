# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: #base class
    def __init__(self, vehicle_name='unkonw'):
        self.vehicle = vehicle_name

class FlightVehicle(Vehicle):
    def __init__(self, Vehicle_name=""):
        super().__init__(Vehicle_name)

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    def __init__(self, Vehicle_name=""):
        super().__init__(Vehicle_name)


# Ground Vehicle class
class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
      

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
     