def solution(a, d, included):
    answer = 0
    for idx, bool in enumerate(included):
        if bool == True:
            print(idx)
            answer += a+ (d*idx)
    return answer