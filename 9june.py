# sets
#unique collection of sets using curled brackets { }

s= {1,2,3,4,5,56,2,4,5,2,5,6}

print(type(s))
print(s)

print(s.pop())
print(s)


fruits={'apple','banana','grapes','orange','chikoo',"stawberry"}
print(fruits)

#diff values in a set

set1=(1,2,3,7,'rays',23.34)
print(set1)

#converting list to set
l=[1,3,56,7,34,786]
set2=set(l)

print(type(l))  #checking the type
print(type(set2)) #checking the type

print(set2) # it becomes a set here

#access set items
for ele in s:
    print(ele)

#add() and update()
color= {'red','blue','black','yellow'}
color.add('pink') #adds an element
print(color)

fruits.update(color) #update in existing set
print(fruits)

#removing(), discarding(), clear(),pop(), del()

fruits.remove('black') #gives error when not avalaible
print(fruits)

fruits.discard('blue') #does not givve error
print(fruits)

fruits.clear() #clears all data from the set
print(fruits)

#del fruits    #deletes entire set from the history.
print(fruits)

#union and intersection

s1={1,2,3,4,5,6,7}
s2={7,8,9,10,11,12}

s3=s1.union(s2)
print(s1)
print(s2)
print(s3)

s4=s1.intersection(s2)
print(s4)

s1.intersection_update(s2)
print(s1)
print(s1.symmetric_difference(s2))
print(s1)

#supersetvalues

y1={1,2,3,4,5,6}
y2={1,2,3,4}
print(y1.issuperset(y2))

print(y2.issubset(y1))

