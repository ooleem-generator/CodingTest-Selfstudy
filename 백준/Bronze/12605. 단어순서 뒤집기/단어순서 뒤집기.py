n = int(input())
for i in range(1, n + 1):
    print("Case", end=" ")
    print(f"#{i}:", end=" ")
    words = list(input().split())[::-1]
    reverse_words = ""
    for w in words:
        reverse_words += f"{w} "
    print(reverse_words)