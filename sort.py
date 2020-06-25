def merge(L, R):
    ans = []
    i = 0
    j = 0
    while (i < len(L)) and (j < len(R)):
        if L[i] <= R[j]:
            ans.append(L[i])
            i += 1
        else:
            ans.append(R[j])
            j += 1
    
    if i == len(L) and j < len(R):
        ans += R[j:]
    elif j == len(R) and i < len(L):
        ans += L[i:]
    return ans

def merge_sort(A):
    if len(A) == 1:
        return A
    else:
        mid = (int)(len(A)/2)
        L = merge_sort(A[:mid])
        R = merge_sort(A[mid:])
        return merge(L, R)

if __name__ == "__main__":
    a = [9,8,7,6,5,4,3,2,1]
    print(merge_sort(a))
    