class ParkingSystem:
    big, medium, small = 0, 0, 0

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType: int) -> bool:
        flag = False
        if carType == 3:
            if self.small > 0:
                flag = True
                self.small -= 1
        elif carType == 2:
            if self.medium > 0:
                flag = True
                self.medium -= 1
        else:
            if self.big > 0:
                flag = True
                self.big -= 1
        return flag




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)