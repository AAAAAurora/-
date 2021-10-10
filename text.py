i=1
j=1
a=[]
b= []
c= []
d= []
e=[]
f=[]
for line in open('C:\\Users\\Aurora\\Desktop\\answer.txt','r',encoding="utf-8") :   
    #print (i)
    a.append(line)
    i=i+1
print (a)

for line in open('C:\\Users\\Aurora\\Desktop\\answer _user.txt','r',encoding="utf-8") :   
    b.append(line)
    j=j+1
print (b)
print ("over1")

k=0
x=0
y=0
n=input("请输入要批改的题目数量 ：")
n = int(n)
while k<n:   
    if a[k]==b[k]:
        c.append(k+1)
        c.append(",")
        x=x+1
    else:
        d.append(k+1)
        d.append(",")
        y=y+1
    print("k=",k)
    k=k+1

del(c[-1])
del(d[-1])

print (c)
print ("\n")
print (d)
print ("\n")
print (x)
print ("\n")
print (y)
e.append(x)
f.append(y)
# ls1=[x for x in c if x!='']
str1 = ''.join(str(m) for m in c)
str2 = ''.join(str(m) for m in d)
str3 = ''.join(str(m) for m in e)
str4 = ''.join(str(m) for m in f)
f=open('C:\\Users\\Aurora\\Desktop\\check.txt','a',encoding="utf-8")
f.write("Correct："+str3+"("+str1+")"+"\n"+"Wrong："+str4+"("+str2+")"+"\n")
f.close()

