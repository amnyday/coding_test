#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* arr[], size_t arr_len) {
    // 모든 문자열의 총 길이를 계산
    size_t total_length = 0;
    for (size_t i = 0; i < arr_len; i++) {
        total_length += strlen(arr[i]);
    }

    // 추가로 널 문자를 위한 공간 확보
    char* answer = (char*)malloc(total_length + 1);
    if (answer == NULL) {
        return NULL; // 메모리 할당 실패 시
    }

    // 문자열 연결
    answer[0] = '\0'; // 초기화
    for (size_t i = 0; i < arr_len; i++) {
        strcat(answer, arr[i]);
    }

    return answer;
}