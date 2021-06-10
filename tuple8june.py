#tuple

t=1,23,4,5,6,78,99,'irfan'
print(type(t))
print(t)

t2=(1,2,445,666,78,453)
print(type(t2))
print(t2)

#t[0]=-1 #no changes allowed after tuple
#print(t) #will show error

#converting list to tuple and vice versa
l=list(t)
print(type(l))

t=tuple(t)
print(type(t))

print(t*5) #to multiply the value by any number

