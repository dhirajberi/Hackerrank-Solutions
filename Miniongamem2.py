def minion_game(string):
    vowel="AEIOU"
    count=0
    count1=0
    for i in range(0,len(string)):
        if(string[i] in vowel):
            count=count+(len(string)-i)
        else:
            count1=count1+(len(string)-i)
    if(count>count1):
        print(f"Kevin {count}")
    elif (count1>count):
        print(f"Stuart {count1}")
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
