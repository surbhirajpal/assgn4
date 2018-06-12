#Q1
'''
i=0
while(i<10):
    num=(input("enter no."))
    print("entered number is "+num)
    i=i+1

#Q2
while(True):
    print("this is infinite loop")
'''
#Q3
a=[]
for i in range (0,5):
    num=int(input("enter number "))
    a.append(num)
print(a)
sq=[]
for i in a:
    numb=(i*i)
    sq.append(numb)
print(sq)



#Q4

l=['hello',13,17.44,'bye',67,89.77]
a=[]
b=[]
c=[]
for i in l:
    if(type(i)==int):
        a.append(i)
    elif (type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)




#Q5
even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even numbers are %s"%even)
print("odd numbers are %s"%odd)


#Q6

for i in range(0, 4):
    for j in range(0, i+1):
        print("*",end=" ")
    print()



#Q7

d={}
n=''
a=''
for i in range (0,3):
    n=input("enter name : ")
    a=int(input("enter age : "))
    d.update({n:a})
for i in d:
    print("keys are %s"%i)
    print("values are %d "%d[i])




#Q8
i=0
c=[]
while(i<5):
    a=int(input("enter numbers "))
    c.append(a)
    i=i+1
a=int(input("enter number to be searched "))
for i in c:
    if(a==i):
        c.remove(i)
print(c)
