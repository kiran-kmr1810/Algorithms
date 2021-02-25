import sys
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        # Copy data to temp arrays L[] and R[]
        l = arr[:mid]
        r = arr[mid:]
        # Recursive calls
        mergesort(l)
        mergesort(r)
        #Merging the temp arrays
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        #Adding remaining elements of the arrays are unequal in size
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
    return arr

a = list(map(int,sys.stdin.readline().split()))
n = len(a)
print(mergesort(a))


# T(n) = 2T(n/2) + θ(n) - case 2 of master method
# Time complexity -> O(nlog(n))
# Space complexity -> O(n)