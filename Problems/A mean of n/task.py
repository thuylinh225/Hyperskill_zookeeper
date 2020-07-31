number = int(input())
total = 0
for _ in range(number):
    x = int(input())
    total += x
mean = total / number
print(float(mean))
