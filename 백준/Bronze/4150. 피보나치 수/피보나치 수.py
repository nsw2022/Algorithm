import sys
sys.setrecursionlimit(10**6)

user = int(input())
dictionary = {1: 1, 2: 1}
# @timeit
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output
print(fibonacci(user))