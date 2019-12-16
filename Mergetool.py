def merge_the_tools(string, k):
    # your code goes here
    sub=len(string)//k
    x=-1
    for j in range(0,sub):
        sum=""
    
        for i in range(0,sub):
            x=x+1
            if(string[x] not in sum):
                sum=sum+string[x]
            
        print(sum)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
