# def solution(my_string, s, e):
#     answer = ''
#     answer += my_string[:s]
#     answer += my_string[e:s-1:-1]
#     if len(my_string) > e+1 :
#         answer += my_string[e+1:]
#     return answer

def solution(my_string, s, e):
    answer = ''
    
    # s 이전 부분 추가
    answer += my_string[:s]
    
    # s부터 e까지 역순으로 추가
    answer += my_string[s:e+1][::-1]
    
    # e 이후 부분 추가
    if len(my_string) > e + 1:  # e 다음 부분이 있으면 추가
        answer += my_string[e+1:]
    
    return answer