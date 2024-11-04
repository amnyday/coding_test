def solution(names):
    answer = []
    for c in names[::5]:
        answer.append(c)
    return answer