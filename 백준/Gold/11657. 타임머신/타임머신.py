v, e = map(int, input().split())
edges = []
distance = [float("inf")] * (v + 1)
for _ in range(e):
    edges.append(tuple(map(int, input().split())))


def bellman_ford(start_node):
    distance[start_node] = 0
    for i in range(v + 1):
        for start, end, weight in edges:
            if distance[start] == float("inf"):
                continue
            if distance[end] > distance[start] + weight:
                distance[end] = distance[start] + weight
                if i == v:
                    print(-1)
                    return
        # print(distance)
    for i in range(2, len(distance)):
        if distance[i] == float("inf"):
            print(-1)
        else:
            print(distance[i])

bellman_ford(1)