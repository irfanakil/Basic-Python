s1 =input("enter a string\n")
s2 =input("enter a string\n")
print(s1*3) #repeat
print(s1+"Is equal to: "+s2+"=",s1.__eq__(s2))#check for same content
print(s1+"Greater than equal to: "+s2+"=",s1.__ge__(s2))
print(s1+"Less than equal to: "+s2+"=",s1.__le__(s2))

s="IRFAN SHAIKH"
for temp in s :
    print(temp)