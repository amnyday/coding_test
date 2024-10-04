
import sys
input = sys.stdin.readline
from collections import deque

# 정점의 수
V = int(input())
# 간선의 수
E = int(input())

# 인접 리스트 표현
graph = []
for _ in range(V+1):
    graph.append([])

# 간선의 정보 E개
for _ in range(E):
    start, end = list(map(int,input().split()))
    graph[start].append(end)
    graph[end].append(start)

start = 1

# 탐색을 몇 번 진행하는지 저장할 변수
count = 0 

stack = []
stack.append(start)
visited = set()
visited.add(start)

while stack:
    node = stack.pop()
    # print(node)
    count += 1
    
    # 인접 노드 순회
    for adj_node in graph[node]:
        # 인접 노드 방문 확인
        if adj_node not in visited:
            visited.add(adj_node)
            stack.append(adj_node)

print(count - 1)