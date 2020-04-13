from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

def dp(streak, i):
    if i >= N:
        return streak
    new_streak, cup = [], cups[i]
    new_streak.append(max(streak[0], streak[1], streak[2]))
    new_streak.append(max(streak[0] + cup, streak[1]))
    new_streak.append(streak[1] + cup)
    return dp(new_streak, i+1)


N, cups = int(input()), []
for _ in range(N):
    cups.append(int(stdin.readline().rstrip()))
if N < 3:
    cups += [0] * (3-N)
streaks = [cups[0] + cups[1], cups[0] + cups[2], cups[1] + cups[2]]
print(max(dp(streaks, 3)))
