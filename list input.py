print("\nEnter the list with sqare brackets like 2,3,[4,5],6 (excluding exterior most sqare brackets):")
l=[str(x) for x in input().split(",")]
for i in range(len(l)):
    if l[i].isnumeric():
        l[i]=int(l[i])
    else:
        t1=l[i].split("[")
        if t1[0]!="":
            t1=l[i].split("]")
        print(t1)
        j=0
        for j in range(len(t1)):
            if t1[0]=='':
                t=t1[-1]
            elif t1[1]=='':
                t=t1[0]
            l[i]=int(t)
print(l,"\n",type(l[2]),len(l))
