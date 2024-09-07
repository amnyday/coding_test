def solution(num_list):
    even = ''
    odd = ''
    
    for i in num_list:
        if i % 2 == 0:  # 짝수일 때
            even += str(i)
        else:  # 홀수일 때
            odd += str(i)
    
    # 빈 문자열에 대한 처리를 위해 조건 추가
    even_sum = int(even) if even else 0
    odd_sum = int(odd) if odd else 0
    
    answer = even_sum + odd_sum
    return answer
