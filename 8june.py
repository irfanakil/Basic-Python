#listing methods


list=[1,23,45,65,43]
print(list)
list.sort()
print(list)

list.sort(reverse= True)
print(list)

#add more than 1 element
points=(2,4,5,6,98)
list.extend(points)
print(list)

list.sort() #for ascending order
print(list)

list2= [34324,245,23542,5546355]
#adding 2 lists
list3 = list + list2
print(list3)


#removing element: particular element
print(list3.remove(1))
print(list3)

#pop element: the last one gets removed
print(list3.pop())
print(list3)

#clear : clears all
print(list3.clear)
print(list3)


#slicing method
print(list)
print(list[::]) #all elements(list)
print(list[2:6])#from 2(icnluded) to 6(excluded)
print(list[:8])# from beginning to 8th
print(list[-1]) #last element
print(list[::-1])#reverse order
print (list[0::1]) #step by 2 (every 2nd element)


#add any temp element step by step
blanklist=[]
print(blanklist)
for e in list:
    blanklist.append(e)
    print(blanklist)

