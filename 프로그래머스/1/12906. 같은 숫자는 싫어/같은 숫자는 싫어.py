def solution(arr):
    if not arr:
        return []
    
    result = [arr[0]]  # 첫 번째 원소를 결과 리스트에 추가
    for num in arr[1:]:
        if num != result[-1]:  # 현재 숫자가 마지막으로 추가된 숫자와 다른 경우
            result.append(num)
    return result