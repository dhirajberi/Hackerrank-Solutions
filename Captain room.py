n=int(input())
grp=list(map(int,input().split(" ")))
for i in range(0,len(grp)):
    if(grp.count(grp[i])!=n):
        x=grp[i]
        break
print(x)

    
