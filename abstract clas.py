from abc import ABC , abstractmethod # ye abstract method ham jis base class me de rhe h usme jo function ham define krenge vhi function hame child class me bhi define krna pdega vo neccessiry ho jatah
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type = "rectangle "
    core = 4
    def __init__(self):
        self.length = 5
        self.breath = 8
    def printarea(self): #abstractmethod ke karan ye yha define krna necessary ho gya to hame ye jarur krna pdta
        return f"{self.length}and {self.breath}"
rc = rectangle()
print(rc.printarea())
