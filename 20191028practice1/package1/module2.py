class module2():
    def __init__(self, arg1, arg2, arg3):
        self.x = arg1 + arg2 + arg3

    def plus(self):
        return(self.x)

    def minus(self):
        return(-self.x)

if __name__ == "__main__":
    print(module2(1,2,3).plus())
    print(module2(1,2,3).minus())