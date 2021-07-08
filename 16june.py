#pass by reference

def changelist():
    print (id(l))
    l.append(6,7)
    print(l)

list=[1,2,3,4,5]
print('-------------before----------------')
print('id is',id(list))
print('------after------')

changelist(list):