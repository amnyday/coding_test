def solution(num_list):
    sum1 = 0
    sum2 = 0
    for i in num_list[::2]:
        sum1+= i
    for j in num_list[1::2]:
        sum2+= j
    return sum1 if sum1> sum2 else sum2