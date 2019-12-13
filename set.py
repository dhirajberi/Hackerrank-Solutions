def average(array):
    sum=0
    avg=0
    s=set(array)
    for value in s:
        sum=sum+value
    avg=sum/len(s)
    return avg
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
