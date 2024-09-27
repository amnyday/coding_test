#힙 자료형 모듈 불러오기
import heapq

import sys
input = sys.stdin.readline

#힙(heap) + 큐(queue)

#정수 1개입력
N = int(input())

#정수를 저장할 힙(heap)
heap = []
# heapq.heapify(heap)

#다음 N개의 줄 == N번 반복문
for _ in range(N):
    #정수 1개 입력
    x = int(input())

    #x가 0일때 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우
    if x == 0 :
        if  len(heap) ==0 :
            print(0)
        else:
            min_number = heapq.heappop(heap)
            print(min_number)
    #x가 0이 아닐때 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
    elif x != 0:
        heapq.heappush(heap,x)
        