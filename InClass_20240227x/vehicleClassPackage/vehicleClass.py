#vehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: we need to add maximum speed to the model
    Change Order: we need a way to 'read' the maximum speed from the model
    Change Order: some developers need to use the constructor without having to provide a max speed
    '''

    def __init__(self, type, max_speed = None):
        '''
        @param: type: the kind of vehicle
        @Param max_speed: maximum speed of the vehicle, defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42
        self.max_speed = max_speed
        
    def printType(self):
        print(self.type);
    
    def getSpeed(self):
        return self.max_speed
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass
