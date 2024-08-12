def solution(str1, str2):
    answer = ''
    for i in range(len(str1)+len(str2)):
        answer += (str1[i] if i < len(str1) else '') + (str2[i] if i < len(str2) else '')
        
    return answer