import sys
num = int(input())
location = []

count = 1
for i in range(num):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    location.append([x,y])

location.sort()
for i in range(0,len(location)):
    print(location[i][0],location[i][1])