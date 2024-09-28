
# 힙 자료형 모듈 불러오기
import heapq
# 힙(heap) + 큐(queue)

import sys
input = sys.stdin.readline

# 정수 1개 입력
N = int(input())

#정수를 저장할 힙(heap)
heap = []
# heapq.heapify(heap)

# N개의 연산 처리
for _ in range(N):
    x = int(input())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            # 가장 큰 값을 출력하려면 음수를 다시 양수로 변환
            print(-heapq.heappop(heap))
    else:
        # 자연수는 음수로 변환하여 최대 힙처럼 작동하게 함
        heapq.heappush(heap, -x)
        