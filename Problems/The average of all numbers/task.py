# put your python code here
a = int(input())
b = int(input())
count = 0
total = 0
for num in range(a, b + 1):
    if num % 3 == 0:
        count += 1
        total += num
        mean = total / count
print(mean)
