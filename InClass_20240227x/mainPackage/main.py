#main.py

from vehicleClassPackage.vehicleClass import *

if __name__ == "__main__":
    myCorvette = Vehicle("Car", 120)
    myCorvette.printType()
    maximumspeed = myCorvette.getSpeed()
    print("Maximum Speed:", maximumspeed)
    
    myDodge = Vehicle("Truck")
    myDodge.printType()
    myCorolla = Vehicle("Car")
    myBoat = Vehicle("Boat")
    mySpaceShip = Vehicle("SpaceShip")
    myVehicles = [Vehicle("Toyota Camry", 150), Vehicle("Sailboat", 20), Vehicle("Falcon Heavy", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())