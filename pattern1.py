# rows = int(input())
# space = ' '
# star = '*'


# --------------------------first method----------------------
# for i in range(rows//2 + 1):
#     print(space * i + star)

# for i in range(rows//2+1, rows):
#     print(space*(rows-i-1) + star)



# --------------------------second method----------------------
# for i in range(rows//2+1):
#     for j in range(i+1):
#         if(i==j):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(rows//2+1, rows+1):
#     for j in range(1,rows-i+1):
#         if(rows-i==j):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()




# print("charu"== ("Charu"))
# print("charu"== ("charu",))
# print(("charu",)== "charu")


# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*', end = " ")
#     print()



# n = int(input())
# for i in range(n,0, -1):
#     for j in range(i):
#         print('*', end = " ")
#     print()




# n = int(input())
# star = '*'
# space = ' '
# for i in range(1,n+1):
#     print(space * (n-i) + star*i)



# n = int(input())
# star = '* '
# space = ' '
# for i in range(1,n+1):
#     print(space*(n-i) + star * i)


# n = int(input())
# star = '*'
# space = ' '
# for i in range(n+1):
#     print(space * (n-i) + star*i)
# for i in range(n-1, 0, -1):
#     print(space *(n-i) + star*i)



# n = int(input())
# star = '*'
# space = ' '
# for i in range(n+1):
#     print(star*i + space*(n-i))
# for i in range(n-1, 0, -1):
#     print(star*i + space *(n-i) )


# ascii = 65
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print(chr(ascii+i), end=" ")
#     print()




# from math import factorial

# n = int(input())
# for i in range(n):
#     for j in range(n-i+1):
#         print(end =" ")
#     for j in range(i+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     print()




# for i in range(n+1):
#     print(space * (n-i) + star*i)

# for i in range(n-1, 0, -1):
#     print(space *(n-i) + star*i)



# num = int(input())
# flag = False
# for i in range(2, num):
#     if(num%i == 0):
#         flag = True
#         break
# if flag: print("Not prime")
# else:
#     print("Prime")



# num = int(input())
# rev = 0
# while(num>0):
#     rem = num%10
#     rev = rev*10 + rem
#     num = num//10
# print(rev)






n = int(input())
star = "* "
space = "  "
for i in range(n):
    if(i==0 or i==n-1 or j==1 or j==n-1):
        print(star*n, end="\n")
    else:
        print(space * (n-2))
