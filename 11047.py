N, M = [int(x) for x in input().split()]
nums = [int(input()) for _ in range(N)]
sum = 0
for num in reversed(nums):
    quotient, M = divmod(M, num)
    sum += quotient
    if M == 0:
        break
print(sum)
