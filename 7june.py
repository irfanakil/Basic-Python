# list data type
#testlist

l=[1,2,3,4,5]
print(type(l))

l2=['rays', 212,435]
print(type(l2))

print('no of elements:', len(l2))

#append adds in the end
l2.append(3455)
print(l2)

#Insert at specific place
l2.insert(0,"alpha")
print(l2)

#replace

#index
print('index of 1:',l2.index(1))
l2.append(2)

#8june contd

print('reverse list:', l2.reverse(1))
print(l2)
