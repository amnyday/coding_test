#백준용 입력 코드
N,K = list(map(int,input().split()))
numbers = list(map(int,input().split()))

#슬라이딩 윈도우를 위한 첫 구간의 합
split_sum = sum(numbers[:K])
#print(split_sum)

#모든 구간 합을 리스트에 저장 후 max() 함수 사용
#첫번째 구간합도 넣어야한다.
answer_list = [split_sum]

#기준위치 i를 순회할 반복문
#0->N-K
for i in range(0, N-K):
    split_sum = split_sum - numbers[i] + numbers[i+K]
    # print(split_sum)
    #모든구간합을 저장한다.
    answer_list.append(split_sum)

print(max(answer_list))