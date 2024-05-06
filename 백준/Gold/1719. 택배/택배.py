import sys
import heapq
from collections import defaultdict

# 상수 정의
MAX_VAL = sys.maxsize
MAX_INT = 201

# 시간 복잡도: O(n^2 * log(m))
# 공간 복잡도: O(m)
# 사용한 알고리즘: 다익스트라 알고리즘, 경로 추적
# 사용한 자료구조: 인접 리스트

# 정점의 거리 정보를 담는 리스트
# d[i] = l, 시작 정점에서 정점 i까지의 거리는 l
distances = [MAX_VAL] * MAX_INT

# 간선 정보를 저장하는 인접 리스트
graph = defaultdict(list)

# 경로 추적을 위한 리스트, parent[i] = j, 정점 j에서 정점 i로 왔습니다.
parents = [0] * MAX_INT

def dijkstra(start_node, n):
    """주어진 시작 노드로부터 다익스트라 알고리즘 수행"""
    # 거리 정보 초기화
    for i in range(1, n + 1):
        distances[i] = MAX_VAL
    distances[start_node] = 0

    # 우선순위 큐 사용 (heapq는 최소 힙)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))

    while priority_queue:
        cur_cost, cur_node = heapq.heappop(priority_queue)

        # 현재 노드의 인접 노드 탐색
        for next_node, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost

            # 더 짧은 경로가 발견되면 거리 정보 갱신 및 부모 노드 추적
            if distances[next_node] > new_cost:
                distances[next_node] = new_cost
                parents[next_node] = cur_node
                heapq.heappush(priority_queue, (new_cost, next_node))

def print_paths(start_node, n):
    """각 시작 노드에서 다른 노드들로의 경로를 출력"""
    for i in range(1, n + 1):
        if i == start_node:
            print("-", end=" ")
        elif parents[i] == start_node:
            print(i, end=" ")
        else:
            cur_node = i
            while True:
                if parents[cur_node] == start_node:
                    print(cur_node, end=" ")
                    break
                else:
                    cur_node = parents[cur_node]
    print()

# 메인 로직 시작
if __name__ == "__main__":
    n, m = map(int, input().split())

    # 간선 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 모든 정점에 대해 다익스트라 알고리즘 수행
    for start_node in range(1, n + 1):
        dijkstra(start_node, n)
        print_paths(start_node, n)
