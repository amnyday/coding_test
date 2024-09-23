import sys
input = sys.stdin.readline

'''
입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 
'''

#여는괄호 => 스택에 저장
#닫는괄호 => 스택 마지막 값을 확인해서 여는괄호면 스택에서 빼서 삭제한다.

#테스트 케이스의 수
T = int(input())

#문자열 순회
for _ in range(T):
    # 스택
    stack = []

    # flag 변수
    flag  = False

    #괄호 문자열 입력
    string = input()
    
    #문자열 순회
    for char in string:
        # char가 ( 이냐
        if char == '(':
            #스택에 저장한다.
            stack.append(char)
        # char가 ) 이냐
        elif char == ')':
            #스택에 ( 있는지 없는지 없는데 -1인덱싱하면 오류나기때문에
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                #비정상적인 문자열
                flag = True
                     
    if flag == True or len(stack) != 0:
        print("NO")
    else:
        print("YES")
