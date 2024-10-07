def solution(numbers, target):
    answer = []
    #방문처리변수
    visited = [False] * len(numbers)
    
    def dfs(node,total):
        if node == len(numbers):
            if total == target:
                #print(total)
                answer.append(total)
            return
        
        number = numbers[node]
    
        #방문처리를 안해도 되는이유?
        dfs(node+1, total+number)
        dfs(node+1, total-number)
        
    #시작 위치(인덱스,노드)
    start = 0
    #값을 더하거나 뺄 기준 변수
    total = 0
    
    dfs(0,0)
    
    return len(answer)