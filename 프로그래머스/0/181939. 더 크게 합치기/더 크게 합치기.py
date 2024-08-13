def solution(a, b):
    # 문자열로 변환 후 연결하여 정수로 변환
    elements1 = int(f"{a}{b}")  # a ⊕ b
    elements2 = int(f"{b}{a}")  # b ⊕ a

    # a ⊕ b와 b ⊕ a 중 더 큰 값을 반환, 같으면 a ⊕ b를 반환
    return max(elements1, elements2)