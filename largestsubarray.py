import numpy as np

def find_max_crossing_subarrary(A, low, mid, high):
    left_sum = -np.inf
    sum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            max_left =  i
            left_sum = sum
    
    right_sum = -np.inf
    sum = 0
    max_right = mid
    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > right_sum:
            max_right = i
            right_sum = sum

    return max_left, max_right, left_sum + right_sum

def find_max_subarrary(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (int)((low + high)/2)
        left_low, left_high, left_sum = find_max_subarrary(A, low, mid)
        right_low, right_high, right_sum = find_max_subarrary(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarrary(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == "__main__":
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    low, high, largest_sub_sum = find_max_subarrary(a, 0, len(a)-1)
    print(low, high, largest_sub_sum)