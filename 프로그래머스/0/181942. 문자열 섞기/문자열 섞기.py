def solution(str1, str2):
    answer = ''
    for i in range(len(str1)+len(str2)): #둘중에작은거만큼 돌면서
        answer += (str1[i] if i < len(str1) else '') + (str2[i] if i < len(str2) else '')
        
    return answer