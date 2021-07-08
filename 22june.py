#exception handling

try:
    print(a)
except NameError as e:
    #print('please define variable before')
    print('error:', e)


#tryelse statements

a=3
try:
    print(a)
except NameError as e:
    print('error{}'.format(e))
    print('alt flow')
else:
    print('successful termination')
finally:
    print('im finally block')

#system defined errors
#module error
#index error #l=[1,23,45,6] l at 34 ?
#value error #a,b,c=1,34,
#attribute error #not defined the list

#custom exceptions

n=int(input('enter a no below 10 and above 0\n'))
try:
    if (n>=1 and n<=10):
        print ('entered no is{}'.format(n))
    else:
        raise Exception('enter proper no:')
except Exception as e:
    print('error {}'.format(e))



#login errors #custom exception class

class LoginError(Exception):
    def __init__(self):
        super().__init__('invalid user')

def authenticate(Name="", Password=""):
    try:
            if(Name.__eq__("admin") and Password.__eq__("abc1234")):
                    print("welcome", Name)
            else:
                raise LoginError()
    except LoginError as e:
            print("Login Error {}".format(e))

authenticate("asd","erwr" )
