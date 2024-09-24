import string

upper_ = list(string.ascii_uppercase)
lower_ = list(string.ascii_lowercase)

def solution(my_string):
    answer = []  # answer 리스트를 함수 내부에서 초기화

    # 대문자 개수 세기
    for S in upper_:
        answer.append(my_string.count(S))

    # 소문자 개수 세기
    for s in lower_:
        answer.append(my_string.count(s))

    return answer