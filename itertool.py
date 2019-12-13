from itertools import product

all=[int(i) for i in input().split(" ")]
all1=[int(i) for i in input().split(" ")]
x=()

x=tuple(product(all,all1))
for value in x:
    print(value,end=" ")
