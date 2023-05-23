arr = [12, 13, 20, 14, 9, 1, 0]
maxi = max(arr)
print(maxi)

maxi = arr[0]

for i in range(1, len(arr)):
    if maxi < arr[i]:
        maxi = arr[i]

print(maxi)

arr.sort()
print(arr)

