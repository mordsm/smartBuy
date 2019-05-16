class Attribute:
    def __gt__(self, other):
        if (self.c_value > other.c_value):
            return True
        else:
            return False
    def __lt__(self, other):
        if (self.c_value < other.c_value):
            return True
        else:
            return False
    def get_cordinated_value(self):
        if isinstance(self.type, int):
            self.c_value = self.value


        if isinstance(self.type, bool):
            if self.value == True:
                self.c_value = 1
            else:
                self.c_value = 0

    def __init__(self, typ, name, value):
        self.value = value
        self.name = name
        self.type = typ
        self.c_value = self.get_cordinated_value()



ob1 = A(2)
ob2 = A(3)
if (ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")