n = int (input())
temp = n
rev = 0

while(n>0):
    rem = n%10
    rev = rem + rev*10
    n = n//10

if rev == temp:
    print("It is pallindrome")

else:
    print("Not a pallindrome")