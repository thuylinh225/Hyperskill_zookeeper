n = int(input())
r = int(input())
count = 0
while n > r:
    n = n // 2
    count += 1
print(count * 12)
