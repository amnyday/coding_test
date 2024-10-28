def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):  
        row = my_string[i:i+m]            
        answer += row[c-1]            
    return answer