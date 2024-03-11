n = int(input()) # 입력받는수
count = 0 # 입력받는 조건을 세줄 변수
s = '666'
i = 0 # 상태변수
while True:
    if s in str(i): # 666포함한 문자가있음 카운트를 세서 리턴
        count += 1
        if count == n: # 카운트를 세줄 변수
            break
    i += 1 # 상태변수를 더해줌
    # print(i)#중간디버깅
print(i) # 결과출력