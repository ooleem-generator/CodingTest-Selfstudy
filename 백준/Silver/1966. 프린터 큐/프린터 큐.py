import sys
from collections import deque

input = sys.stdin.readline

testcases = int(input())
for _ in range(testcases):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    print_queue = deque()
    count = 0

    for i, v in enumerate(docs):
        print_queue.append((v, i))

    # print(print_queue)

    while len(print_queue) > 0:
        doc_staged = print_queue.popleft()
        # print(doc_staged)
        for doc in print_queue:
            if doc[0] > doc_staged[0]:
                print_queue.append(doc_staged)
                # print(print_queue)
                break
        else:
            count += 1
            # print(f"{doc_staged} 출력됨, 현재 출력 문서 수 : {count}")
            if doc_staged[1] == m:
                print(count)
                break
