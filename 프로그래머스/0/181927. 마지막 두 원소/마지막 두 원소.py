def solution(num_list):
    answer = num_list

    if len(num_list) > 1: #2개이상있어야 두개 비교하니까
        answer.append(num_list[-1] - num_list[-2] if num_list[-1] > num_list[-2] else num_list[-1] *2) 
    return answer
