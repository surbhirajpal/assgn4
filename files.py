#Q1
'''
f=open("text.txt",encoding="utf-8")
n=int(input("enter number of last lines you want to be printed"))
l=f.readlines()
l.reverse()
print(l[:n])
f.close()


#Q2
word = input("Enter word to be searched:")
k = 0
f=open("text.txt",encoding="utf-8")
for line in f:
    words = line.split()
    for i in words:
        if (i == word):
            k = k + 1
print("Occurrences of the word:")
print(k)
f.close()


#Q3
f=open("text.txt",encoding="utf-8")
a=open("file.txt",'r+')
f1=f.readlines()
for i in f1:
    a.write(i)
print(a.read())
f.close()
a.close()


#Q4
x=open("text.txt",encoding="utf-8")
y=open("text1.txt",encoding="utf-8")
z=open("add.txt",'r+')
x1=x.readlines()
y1=y.readlines()
for i,j in zip(x1,y1):
    z.write(i+j)
    print(i+j)
x.close()
y.close()
z.close()
'''

#Q5
import random
i=0
x=open("1.txt",'r+')
y=open("2.txt",'r+')
l=[]
for i in range(10):
    l.append(random.randrange(0,100))
    l[i]=str(l[i])
print(l)
print(sorted(l))
x.writelines(l)
print(x.readlines())
y.writelines(sorted(l))
print(y.readlines())
x.close()
y.close()
