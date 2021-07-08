from threading import Thread
from math import factorial
class Fact(Thread):
    def __init__(self,number):
        super().__init__()
        self.number=number

    def run(self):
        print("factorial of {} is = {}".format(self.number,factorial(self.number)))

t1=Fact(5)
t2=Fact(10)
t3=Fact(15)

t1.start()
t2.start()
t3.start()




