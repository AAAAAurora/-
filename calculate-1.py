from math import ldexp
import random
import math
from fractions import Fraction

def number(range):
    #生成随机数（范围由用户决定）
    x=random.randrange(0,5)
    #生成整数
    if x<=4: 
        num=random.randrange(0,range)
        #生成分数
    else:
        a=random.randrange(0,range)
        b=random.randrange(1,range)
        #保证生成的是真分数
        if a<=b:
            num=Fraction(a,b)
        else:
            num=Fraction(b,a)
            

    return num

def sign():
    #生成随机运算符
    list=['+','-','*','/']
    sign=random.choice(list)
    return sign


def cal_1(n1,sign,n2):
    right=1
    if sign=='+':
        res=n1+n2
    if sign=='-':
        res=n1-n2
        if n1>n2: 
            right=1
        else:
            right=0
    if sign=='*':
        res=n1*n2
    if sign=='/' and n2!=0:
        res=Fraction(n1,n2)
    if sign=='/' and n2==0:
       res=0
       right=0
    return res,right

def cal_2(a,s1,b,s2,c):
    right=1
    if s1=="+" or s1=="-":
        x=0
    else:
        x=1
    if s2=="+" or s2=="-":
        y=0
    else:
        y=1
    if x^y==0 or x==1: 
        res1,right=cal_1(a,s1,b)
        res,right=cal_1(res1,s2,c)
    else:
        res1,right=cal_1(b,s2,c)
        res,right=cal_1(a,s1,res1)  
    return res,right

def cal1(a,s,b,range):
    res,right=cal_1(a,s,b)
    if right==1 and res>=0:
        print(a,s,b,"=",res)
    arr = [a,s,b,"="]
    str1 = ''.join(str(i) for i in arr)
    return res,right,str1

def cal2(a,s1,b,s2,c,range):
    bar_list = ['有括号', '无括号']
    bar = random.choice(bar_list)
    if bar=='无括号':
        if s1=="+" or s1=="-":
            x=0
        else:
            x=1
        
        if s2=="+" or s2=="-":
            y=0
        else:
            y=1

        if x^y==0 or x==1: 
            res1,right=cal_1(a,s1,b)
            res,right=cal_1(res1,s2,c)
        else:
            res1,right=cal_1(b,s2,c)
            res,right=cal_1(a,s1,res1)  

        if right==1 and res>=0:
            print(a,s1,b,s2,c,"=",res)
        arr = [a,s1,b,s2,c,"="]
        str1 = ''.join(str(i) for i in arr)
            

    if bar=='有括号':
        post_list = ['front', 'later']
        bar_post=random.choice(post_list) 
        if bar_post=='front':
            res1,right=cal_1(a,s1,b)
            res,right=cal_1(res1,s2,c)
            if right==1 and res>=0:
                print("(",a,s1,b,")",s2,c,"=",res)
            arr = ["(",a,s1,b,")",s2,c,"="]
            str1 = ''.join(str(i) for i in arr)
                
        if bar_post=='later':
            res1,right=cal_1(b,s1,c)
            res,right=cal_1(a,s2,res1)
            if right==1 and res>=0:
                print(a,s2,"(",b,s1,c,")","=",res)
        arr = [a,s2,"(",b,s1,c,")","="]
        str1 = ''.join(str(i) for i in arr)

       
    return res,right,str1


def cal3(a,s1,b,s2,c,s3,d,range):
    bar_list = ['有括号', '无括号']
    bar = random.choice(bar_list)

    
    if s1=="+" or s1=="-":
        x=0
    else:
        x=1
        
    if s2=="+" or s2=="-":
        y=0
    else:
        y=1
    if s3=="+" or s3=="-":
        z=0
    else:
        z=1
    if bar== '无括号':
        if x==0 and y==0 and z==0:
             #符号相同顺序执行
            res1,right=cal_1(a,s1,b)
            res2,right=cal_1(res1,s2,c)
            res,right=cal_1(res2,s3,d) 
    
        if x==1 and y==1 and z==1:
             #符号相同顺序执行
            res1,right=cal_1(a,s1,b)
            res2,right=cal_1(res1,s2,c)
            res,right=cal_1(res2,s3,d) 

        if x==1 and y==0 and z==0:
            res1,right=cal_1(a,s1,b)
            res2,right=cal_1(res1,s2,c)
            res,right=cal_1(res2,s3,d)
        if x==0 and y==1 and z==0:
            res1,right=cal_1(b,s2,c)
            res2,right=cal_1(a,s1,res1)
            res,right=cal_1(res2,s3,d)
        if x==0 and y==0 and z==1: 
            res1,right=cal_1(c,s3,d)
            res2,right=cal_1(a,s1,b)
            res,right=cal_1(res2,s2,res1)
        if x==1 and y==1 and z==0:
            res1,right=cal_1(a,s1,b)
            res2,right=cal_1(res1,s2,c)
            res,right=cal_1(res2,s3,d)
        if x==0 and y==1 and z==1:
            res1,right=cal_1(b,s2,c)
            res2,right=cal_1(res1,s3,d)
            res,right=cal_1(a,s1,res2)
        if x==1 and y==0 and z==1:
            res1,right=cal_1(a,s1,b)
            res2,right=cal_1(c,s3,d)
            res,right=cal_1(res1,s2,res2)

        if right==1 and res>=0:
            print(a,s1,b,s2,c,s3,d,"=",res)
        arr = [a,s1,b,s2,c,s3,d,"="]
        str1 = ''.join(str(i) for i in arr)

    if bar=='有括号':
        case=random.randrange(1,10)
        if case==1:
                res1,right=cal_1(a,s1,b)
                res,right=cal_2(res1,s2,c,s3,d)
                if right==1 and res>=0:
                    print("(",a,s1,b,")",s2,c,s3,d,"=",res)
                arr = ["(",a,s1,b,")",s2,c,s3,d,"="]
                str1 = ''.join(str(i) for i in arr)
                    
        if case==2:
                res1,right=cal_1(b,s2,c)
                res,right=cal_2(a,s1,res1,s3,d)
                if right==1 and res>=0:
                    print(a,s1,"(",b,s2,c,")",s3,d,"=",res)
                arr = [a,s1,"(",b,s2,c,")",s3,d,"="]
                str1 = ''.join(str(i) for i in arr)
        if case==3:
                res1,right=cal_1(c,s2,d)
                res,right=cal_2(a,s1,b,s2,res1)
                if right==1 and res>=0:
                    print(a,s1,b,s2,"(",c,s3,d,")","=",res)
                arr = [a,s1,b,s2,"(",c,s3,d,")","="]
                str1 = ''.join(str(i) for i in arr)
        if case==4:
                res1,right=cal_2(a,s1,b,s2,c)
                res,right=cal_1(res1,s3,d)
                if right==1 and res>=0:
                    print("(",a,s1,b,s2,c,")",s3,d,"=",res)
                arr = ["(",a,s1,b,s2,c,")",s3,d,"="]
                str1 = ''.join(str(i) for i in arr)
        if case==5:
                res1,right=cal_2(b,s2,c,s3,d)
                res,right=cal_1(a,s1,res1)
                if right==1 and res>=0:
                    print(a,s1,"(",b,s2,c,s3,d,")""=",res)
                arr = [a,s1,"(",b,s2,c,s3,d,")""="]
                str1 = ''.join(str(i) for i in arr)
        if case==6:
                res1,right=cal_1(a,s1,b)
                res2,right=cal_1(c,s3,d)
                res,right=cal_1(res1,s2,res2)
                if right==1 and res>=0:
                    print("(",a,s1,b,")",s2,"(",c,s3,d,")","=",res)
                arr = ["(",a,s1,b,")",s2,"(",c,s3,d,")","="]
                str1 = ''.join(str(i) for i in arr)
        if case==7:
                res1,right=cal_1(a,s1,b)
                res2,right=cal_1(res1,s2,c)
                res,right=cal_1(res2,s3,d)
                if right==1 and res>=0:
                    print("(","(",a,s1,b,")",s2,c,")",s3,d,"=",res)
                arr = ["(","(",a,s1,b,")",s2,c,")",s3,d,"="]
                str1 = ''.join(str(i) for i in arr)
        if case==8:
                res1,right=cal_1(b,s2,c)
                res2,right=cal_1(a,s1,res1)
                res,right=cal_1(res2,s3,d)
                if right==1 and res>=0:
                    print("(",a,s1,"(",b,s2,c,")",")",s3,d,"=",res)
                arr = ["(",a,s1,"(",b,s2,c,")",")",s3,d,"="]
                str1 = ''.join(str(i) for i in arr)
        if case==9:
                res1,right=cal_1(b,s2,c)
                res2,right=cal_1(res1,s3,d)
                res,right=cal_1(a,s1,res2)
                if right==1 and res>=0:
                    print(a,s1,"(","(",b,s2,c,")",s3,d,")","=",res)
                arr = [a,s1,"(","(",b,s2,c,")",s3,d,")","="]
                str1 = ''.join(str(i) for i in arr)
        if case==10:
                res1,right=cal_1(c,s3,d)
                res2,right=cal_1(b,s2,res1)
                res,right=cal_1(a,s1,res2)
                if right==1 and res>=0:
                    print(a,s1,"(",b,s2,"(",c,s3,d,")",")","=",res)
                arr = [a,s1,"(",b,s2,"(",c,s3,d,")",")","="]
                str1 = ''.join(str(i) for i in arr)

   
    return res,right,str1

def fraction(n):
    k=math.floor(n)
    f=n-k
    return k,f



if __name__ == '__main__':
    # f = open('C:\\Users\\86139\\Desktop\\question.txt','w',encoding="utf-8")
    n=input("题目数量 ：")
    r=input("计算范围 ：")
    n = int(n)
    r = int(r)
    #python中input函数输出的是一个字符串，而只有通过int进行强制转换

    a=number(r)
    b=number(r)
    c=number(r)
    d=number(r)
    s1=sign()
    s2=sign()
    s3=sign()

    count=1
    while (count<=n):
    #生成的符号个数
        x=random.randrange(1,30)
        a=number(r)
        b=number(r)
        c=number(r)
        d=number(r)
        s1=sign()
        s2=sign()
        s3=sign()

        if x<=10:
            res,right,string=cal1(a,s1,b,r)
    
        if x>10 and x<=20:
            res,right,string=cal2(a,s1,b,s2,c,r)

    
        if x>20 and x<=30:
            res,right,string=cal3(a,s1,b,s2,c,s3,d,r)
        
        
        
        if right==1 and res>=0:
            
            arr = [count]
            str1 = ''.join(str(j) for j in arr)

            f=open('C:\\Users\\Aurora\\Desktop\\question.txt','a',encoding="utf-8")
            f.write("题目"+str1+"："+string+"\n")
            f.close()

    
            int,fra=fraction(res)  #约分处理
            if fra==0 or int==0 :
                arr = [res]
            else: 
                arr = [int,"'",fra]

            str2 = ''.join(str(j) for j in arr)

            f=open('C:\\Users\\Aurora\\Desktop\\answer.txt','a',encoding="utf-8")
            f.write("答案"+str1+"："+str2+"\n")
            f.close()
            count=count+1
        #print(res)
        
        #num[i]=res
        #print(num[i])


    #     "s"=res
    #     f.write(s"\n ")
    # f.close()
    
    