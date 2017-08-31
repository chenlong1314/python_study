#coding:utf-8

id= input("Enter your id:")
l=[]
for i in id:
    l.append(i)
k=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
for p in range(len(k)):
    sum=sum+(int(l[p])*k[p])
w=sum%11
m=[0,1,2,3,4,5,6,7,8,9,10]
n=[1,0,'x',9,8,7,6,5,4,3,2]
for j in range(len(m)):
    if str(m[j]) == str(w) :
        if str(n[j]) == l[17]:
            print("可以开房的身份证！")
        else:
            print("假的吧")

