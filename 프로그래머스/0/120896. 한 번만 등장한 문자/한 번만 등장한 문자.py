def solution(s):
    
    # for c in s:
    #     if c not in dic.keys():
    #         dic[c] = 1
    #     elif c in dic.keys():
    #         dic[c] = dic[c] +1
    # for key in dic:
    #     value = dic[key]
    #     if value ==1:
    #         answer += key
            
    
    from collections import defaultdict
    answer = ''
    
    #문자열 개수 저장 딕셔너리
    dict_ = defaultdict(int)
    #문자열 순회
    for c in s:
        #문자(c) 개수 카운팅
        dict_[c] += 1
    #value가 1인 key탐색
    for key,value in sorted(dict_.items()):
        if value == 1:
            answer += key
    #문자열 정렬
    #정렬함수 sorted() 활용
    #sorted(컨테이너 자료형)는 정렬된 리스트를 반환
    #answer = sorted(answer)
    #리스트->문자열로 형변환
    #join() 매서드 활용
    #''.join(리스트) : 리스트의 각원소를 연결해서 문자열을 생성
    answer = ''.join(answer)
    return answer