N, X, Y = map(int,input().split())

count = 0
for i in range(N):
    if (i+1) % X == 0 or (i+1) % Y == 0:
        count += 1
print(count)