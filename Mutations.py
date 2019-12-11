def mutate_string(string, position, character):
    new=list(string)
    new[position]=character
    new="".join(new)
    return new

if __name__ == '__main__':
    s=input()
    i,c=(input().split())

    print(mutate_string(s,int(i),c))
