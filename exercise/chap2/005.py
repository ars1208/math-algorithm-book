N = int(input())
A = list(map(int,input().split()))

s = 0
for i in A:
  s += i
print(s % 100)