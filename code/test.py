##def temp_conversion(c):
##    f=c*1.8+32
##    return f
##c=float(input("请输入摄氏度:"))
##f=temp_conversion(c)
##print("转换的华氏度为：",f)

##score=input("请输入你的分数：")
##score=int(score)
##if score==100:
##    print("S")
##elif 90 <= score < 100:
##    print("A")
##elif 80 <= score < 90:
##    print("B")
##elif 70 <= score < 80:
##    print("C")
##elif score < 70:
##    print("D")
##else:
##    print("请输入1-100的分值")

##age=16
##if age<18:
##    print("未满18不能观看")
##else:
##    print("欢迎观看！")
##age=16
##print("未满18不能观看") if age<18 else print("欢迎观看！")
##

##score=85
##level=('D' if 0<=score<60 else
##       'C' if 60<=score<70 else
##       'B' if 70<=score<80 else
##       'A' if 80<=score<100 else
##       'S' if score==100 else
##       "请输入0-100之间的数值")
##print(level)


##age=18
##ismale=False
##if ismale is True:
##    if age>=18:
##        print("可以采购")
##    else:
##        print("未满18，禁止采购")
##else:
##    print("性别不对，禁止采购")


##while True:
##    answer=input('可以推出循环了吗？')
##    if answer=='可以':
##        break

##i=0
##while i<10:
##    i+=1
##    if i%2==0:
##        continue
##    print(i)

##day =1
##while day<=7:
##    answer=input('今天有好好复习吗？')
##    if answer!='有':
##        break
##    day=day+1
##else:
##    print('恭喜完成七天打卡！')

    
##i=1
##while i<=9:
##    j=1
##    while j<=i:
##        print(j,'*',i,'=',i*j,end=" ")
##        j=j+1
##    print()
##    i=i+1
    
##sum=0     
##for i in range(10000001):
##    sum=sum+i
##print(sum)
    

##for n in range(2,10):
##    for x in range(2,n):
##        if n%x==0:
##            print(n,"=",x,"*",n//x)
##            break
##    else:
##            print(n,"是一个素数")


#列表的增删改查
#下标索引
    ##    heros=['钢铁侠','绿巨人']
    ##    heros.append('黑寡妇')
    ##    heros.extend(['鹰眼','灭霸','雷神'])#extend()方法的参数必须是一个可迭代对象
    ##    s=[1,2,3,4,5]
    ##    s[len(s):]=[6]
    ##    s[len(s):]=[7,8,9]
    ##    s.insert(1,2)
    ##    s.insert(len(s),10)
    ##
    ##    heros.remove('灭霸')
    ##    heros.pop(2)#剔除指定位置的值
    ##    heros.clear()#清除列表所有值
    ##
    ##    print(heros)
    ##    print(s)
    ##
    ##    x=['a','b','c','d','e','f','g']
    ##    x[2]='C'
    ##    x[3:]=['D','E','F','G']
    ##
    ##    nums=[3,1,5,7,6,9,1,5,4,]
    ##    nums.sort()
    ##    nums[0]=88
    ##    nums.reverse()
    ##    nums.sort()
    ##    nums.reverse()
    ##
    ##    num=[3,1,5,7,6,9,1,5,4,]
    ##    num.sort(reverse=True)
    ##    num.count(1)
    ##    num[num.index(5)]=100
    ##    num.index(5,3,7)#num.index(元素，开始位置，结束位置)
    ##    num_copy=num.copy()
    ##    print(num_copy)
    ##    print(x)
    ##    print(nums)
    ##    print(num)

    ##    s=[1,2,3]
    ##    t=[4,5,6]
    ##    matrix=[[1,2,3],
    ##            [4,5,6],
    ##            [7,8,9]]
    ##    for i in matrix:
    ##        for each in i:
    ##            #print(each)
    ##            print(each,end=' ')#添加空格和换行
    ##        print()                #添加空格和换行
    ##    print(matrix[0][0]) 
    ##    print(s+t)
    ##    print(s*3)
    ##    print(matrix)


##def AMD(x1,x2):
##    w1,w2,theta=0.5,0.5,0.7
##    tem=x1*w1+x2*w2
##    if tem <=theta:
##        return 0
##    elif tem>theta:
##        return 1
##print(AMD(1,1))
##


a=range(10)
for each in a:
    print(each)



















