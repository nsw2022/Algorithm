# 사용자로부터 여러 개의 정수를 입력받아 리스트 li에 저장
li = list(map(int, input().split()))

# 사용자로부터 정수 x, y, r을 입력받아 변수에 저장
x, y, r = map(int, input().split())

# 만약 x가 리스트 li에 존재하면 해당 인덱스 + 1을 출력하고,
# 그렇지 않으면 0을 출력
print(li.index(x) + 1 if x in li else 0)
