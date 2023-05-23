n = int(input())
star = '*'
space = ' '

for i in range(1,n+1):
    print(space * (n-i) + star)

for i in range(1,n):
    print(space * i + star)