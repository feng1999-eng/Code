# coding=GBK
from cal_time import *
@cal_time
def Linear_sort(lis, val):
    for index, v in enumerate(lis):
        if v == val:
            return index
    return None

@cal_time
def half_search(lis, val):
    low = 0
    high = len(lis) - 1
    lis.sort()
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] == val:
            return mid
        elif lis[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return None


A = [5,2,1,6,4,8,3]
print(half_search(A, 5))
