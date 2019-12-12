import textwrap

def wrap(string, max_width):
    string=textwrap.fill(text=string,width=4)

    return string
    
s=input()
w=int(input())
print(wrap(s,w))
