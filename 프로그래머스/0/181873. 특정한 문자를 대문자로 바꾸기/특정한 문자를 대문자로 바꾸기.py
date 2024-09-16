def solution(my_string, alp):
    # 문자열은 인덱스로 바꿀수없음. 리스트로 변환
    my_string_list = list(my_string)
    
    for idx, char in enumerate(my_string_list) :
        if char == alp: 
            my_string_list[idx] = alp.upper()
            
    return ''.join(my_string_list)