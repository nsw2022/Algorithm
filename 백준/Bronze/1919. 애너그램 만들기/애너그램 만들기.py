def min_removal_for_anagram(word1, word2):
    # 각 단어에서 각 문자의 개수를 세는 함수
    def count_chars(word):
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    
    # 각 단어의 문자 개수를 구함
    count_word1 = count_chars(word1)
    count_word2 = count_chars(word2)
    
    # 두 단어 간의 차이를 계산하여 최소 제거 개수를 구함
    removal_count = sum(abs(count_word1.get(char, 0) - count_word2.get(char, 0)) for char in set(count_word1) | set(count_word2))
    
    return removal_count

# 사용자로부터 두 단어 입력받기
word1 = input()
word2 = input()

# 계산 결과 출력
result = min_removal_for_anagram(word1, word2)
print(result)
