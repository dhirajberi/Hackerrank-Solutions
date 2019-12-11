string=input()
mylist=[]
for i in range(len(string)):
    if(string[i]==string[i].upper()):
        mylist.append(string[i].lower())
    elif(string[i]==string[i].lower()):
        mylist.append(string[i].upper())
    
    
    
for data in mylist:
    print(data,end="")
