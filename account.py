#synchronization

from time import sleep
class Account:
    def __init__(self):
        self.balance=0

    def getBalance(self):
        return self.balance
    def setBalance(self,b):
        self.balance=b

    def deposit(self,amt):
        bal= getBalance()
        setBalance(bal+amt)

from threading import Thread
class RaceCondition(Thread):
    name=""
    acc=Account()


    def __init__(self,n):
        super().__init__()
        self.name=n

    def run(self):
        for x in range(5):
            RaceCondition.acc.deposit(100)
        print("{} Final Bal is {}".format(self.name,acc.getBalance))

t1=RaceCondition("irf")
t2=RaceCondition("ish")

t1.start()
t2.start()