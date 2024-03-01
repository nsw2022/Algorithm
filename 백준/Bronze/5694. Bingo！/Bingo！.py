
def is_possible_to_call_out(N, B, balls_in_bag):
    all_numbers = set(range(N + 1))
    possible_differences = set()
    for i in range(B):
        for j in range(i, B):
            possible_differences.add(abs(balls_in_bag[i] - balls_in_bag[j]))
    return all_numbers==possible_differences

while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0:
        break
    balls_in_bag = list(map(int, input().split()))
    result = is_possible_to_call_out(N, B, balls_in_bag)
    if result:
        print("Y")
    else:
        print("N")
