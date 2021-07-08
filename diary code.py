f=open("MyDiary.txt","a")
import datetime as dt
f.write("Date:{}\n".format(dt.datetime.now()))
flag=True
print("Welcome\n")
while(flag):
    data=input("")
    f.write(data)
    if (data.__eq__("Quit")):
        flag = False
else:
    print("see you soon")

f.close()
