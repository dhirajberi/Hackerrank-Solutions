def minion_game(string):
    # your code goes here
    vowel="AEIOU"
    count=0
    count1=0
    for i in range(0,len(string)):
        if(string[i] in vowel):
            for value in range(i,len(string)):
                count=count+1
        else:
            for value in range(i,len(string)):
                count1=count1+1
    if(count>count1):
        print(f"Kevin {count}")
    elif (count1>count):
        print(f"Stuart {count1}")
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
