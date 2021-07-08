#dictionary values
dic={'name':'Irfan', 'surname':'Shaikh', 'add':'Pune'}
print(type(dic))
#access values
print("address",dic['add'])
print(dic)

#changing values
dic['add']= 'Mumbai'
print(dic)

keys=dic.keys()
print('all keys:',keys)
print('all values{} from dictionary'.format(dic.values()))
print(dic.pop('add'))
print(dic)

print(dic.get('surname'))
print(dic)

a=3
b=3
print(a is b)
print(id(a))
print(id(b))

