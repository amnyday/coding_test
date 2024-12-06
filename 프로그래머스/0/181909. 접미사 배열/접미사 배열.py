def solution(my_string):
    answer = []
    for idx in range(len(my_string)):
        answer.append(my_string[idx:])
    return sorted(answer)