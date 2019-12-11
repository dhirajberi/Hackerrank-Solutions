mytuple=()
x=int(input())
all=[int(i) for i in input().split(" ")]

for value in all:
    mytuple=mytuple+(value,)
print(mytuple.__hash__())
