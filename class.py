class Dog():
    def __init__(self,name):
        self.name=name
    def sit(self):
        print(self.name,"is sitting right now")
d=Dog("Bad")
d.sit()