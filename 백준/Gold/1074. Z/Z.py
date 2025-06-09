n, r, c = list(map(int, input().split()))

def route_finder(N, r, c, min_r, min_c, max_r, max_c, route_tracking):

    if N == 0:
        return route_tracking

    mid_r = (min_r + max_r) // 2
    mid_c = (min_c + max_c) // 2

    if r < mid_r:
        if c < mid_c:  # 1사분면
            route_tracking.append(0)
            max_r = mid_r
            max_c = mid_c
        else:  # 2사분면
            route_tracking.append(1)
            max_r = mid_r
            min_c = mid_c
    else:
        if c < mid_c:  # 3사분면
            route_tracking.append(2)
            min_r = mid_r
            max_c = mid_c
        else:  # 4사분면
            route_tracking.append(3)
            min_r = mid_r
            min_c = mid_c

    route_finder(N - 1, r, c, min_r, min_c, max_r, max_c, route_tracking)
    
    return route_tracking

route = route_finder(n, r, c, 0, 0, 2**n, 2**n, [])
answer = 0
for i in range(len(route)):
    answer += route[::-1][i] * 4**i

print(answer)

    
