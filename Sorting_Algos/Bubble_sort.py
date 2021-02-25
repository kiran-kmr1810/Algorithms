import sys
a = list(map(int,sys.stdin.readline().split()))
n = len(a)
for i in range(n):
    swapped = False #By using SWAPPED variable , we try to avoid unnecassary loops after the list is sorted
    for j in range(0 , n-i-1): #By using range(0,n-i-1), we avoid uncessary checking.
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swapped = True
    if not swapped:
        break
print(a)

# Time complexity -> O(n^2)
# Space complexity -> no extra space taken


        
