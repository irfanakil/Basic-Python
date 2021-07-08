#functions

def helloworld():
    print('hello world')

helloworld()

def helloname(name,age,college):
    print("My name is{}".format(name))
    print('my age is {}'.format(age))
    print('i study in{}'.format(college))

helloname('irfan','25','DY Patil')
print(helloname)

#relative arguments

def sum(a,b):
    sum=(a+b)
    return sum #returns with the answer

value=sum(2,3)
print('sum is', value)

#keyword argument
value=sum(b=3,a=2)
print('sumis', value)

#default arguments
def mul(a=2,b=5):
    return a*b
print('multiply',mul(7,8)) #updated values are considered


#variable length argument

def sumofn(*a):
    sum=0
    for n in a :
        sum+=n
    return sum

result=sumofn(1,2,3,4,5,6,7,8,9,10)
print(result)

def names(*c):
    for names in c :
        print('entered name is{}'.format(c))
#for x in range(1,6):
n=input('the displayed name is\n')
name(n)