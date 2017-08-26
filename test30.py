class Dog(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(('hi, i am %s.')%self.name)

if __name__=='__main__':

    dog=Dog("niyang")
    dog.greet()