stack = []

def push(n) :
    stack.append(n)

def pop():
    if len(stack) > 0 : #stack[0] : 이렇게하면, 인덱스에러
        print(stack.pop())
    else:
        print('-1')

def size() :
    print(len(stack))

def empty() :
    if len(stack) == 0 :
        print(1)
    else:
        print(0)
        
def top():
    if len(stack) > 0 :
        print(stack[len(stack)-1])
    else :
        print(-1)
                
n = int(input())    
    
for i in range(n) :
    str = input()
    a = str.split() #a[0] =push a[1] = 1
    if a[0] =='push' :
        push(a[1])
    elif a[0] == 'pop' :
        pop()
    elif a[0] == 'size' :
        size()
    elif a[0] == 'empty' :
        empty()
    elif a[0] == 'top' :
        top()