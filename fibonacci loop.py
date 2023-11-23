def fibonacci(i):
        a=0
        b=1
        c=0
        for i in range (1, i+1):
            if i==1:
                c=0 
            elif i==2:
                c=1
            else:
                c=a+b
                a=b
                b=c
            print(c)          
        return c
print("Choose a number")
i=13
res=fibonacci(i)