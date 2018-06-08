#Q1
a=(2,5,3.55,"hello",899,"hey")
print(len(a))

#Q2
a=(1,3,5,7)
s=min(a)
l=max(a)
print("smallest element is %s"%(s))
print("largest element is %s"%(l))

#Q3
a=(1,3,5,7)
p=(1*3*5*7)
print("product of tuple (1,3,5,7)is %s"%(p))



#SETS

#Q1
a=input("enter first element of set 1  :")
b=input("enter second element of set 1  :")
c=input("enter first element of set 2  :")
d=input("enter second element of set 2  :")
s1=set([a,b])
s2=set([c,d])
print("set 1 is %s"%(s1))
print("set 2 is %s"%(s2))
d=s1-s2
print("difference is %s"%(d))
s3=s1<=s2
print("is s1 a subset of s2 : %s"%(s3))
s4=s1>=s2
print("is s1 a superset : %s"%(s4))
i=s1&s2
print("intersection of s1 and s2 is %s"%(i))



#DIRECTORIES

#Q1
n=input("enter name ")
s1=input("enter marks in maths ")
s2=input("enter marks in science ")
s3=input("enter marks in english ")
s4=input("enter marks in hindi ")
d={'name':n,
   'maths':s1,
   'science':s2,
   'english':s3,
   'hindi':s4}
print(d)


#Q3
l=("mississippi")
a=l.count("m")
b=l.count("i")
c=l.count("s")
d=l.count("p")
e={'no. of m':a,
   'no. of i':b,
   'no. of s':c,
   'no. of p':d}
print (e)


