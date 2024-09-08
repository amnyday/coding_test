def solution(num_list):
    a = num_list[0]
    b = num_list[0]
    for n in num_list[1:]:
        a *= n
        b += n
    if a < b**2 :
        answer = 1
    else:
        answer = 0
    return answer