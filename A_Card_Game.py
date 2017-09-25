#Harendra Singh

t=input()
while(t>0):
    n=input()
    r=range(1,n+1)
    while(len(r)!=1):
        k=[]
        for i in range(1,len(r),2):
            k = k.append(r[i])
        r=k
    t=t-1
    print(r)

