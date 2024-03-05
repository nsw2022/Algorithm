'''
백준 문제를 풀면서 비문학을 푸는듯한 느낌을 많이 받것 같습니다

문제를 간단히 요약하자면 사전처럼 검색을하는데
처음엔 저장할 길이수 입력, 이후알바펫 입력 다끝나면 정렬이 다되어 보여짐!
중복도 불허

정렬 우선순위
1. 길이
2. 알파벳순으로
'''
import sys
# sys.stdin.readline() input()함수보다 더 빠르다고 합니다
user = int(sys.stdin.readline())
lst = []
for i in range(user):
    lst.append(sys.stdin.readline().strip()) # 공백제거안하면 에러남
set_lst = set(lst) # 문제에 중복도 불허
lst = list(set_lst)
lst.sort()
lst.sort(key = len) # 파라미터는 길이순 정렬 가능 reverse=False(오름차순) 과
# key는 정렬을 인자를 함수로 받는데 lambda로 원하는 형태를 직접 지정을 해도된다.

# 번외로 sort와 sotred 의 메서드가있는데 sort 메서드는 원본을 변형 sotrted는 변형을 시기킨 않는다
for i in lst:
    print(i)# 출력