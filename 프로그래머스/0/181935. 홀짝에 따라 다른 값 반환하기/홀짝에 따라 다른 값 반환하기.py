def solution(n):
    if n&1 :
        return sum(list(range(n,0,-2)))
    else:
        num_lst = list(range(n,0,-2))
        sum_num = sum(x **2 for x in num_lst)
        return sum_num
            
    