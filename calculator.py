#Creating a calculator with basic functions like adding, multiplying, subtracting, and divisoning

class Calculator:

    def calAdd(self, x, y):
        return x +y

    def calMutiply(self, x, y):
        return x *y
    
    def calSubtract(self, x, y):
        return x -y
    
    def calDivide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Zero cannot be divdied")
        return x /y
