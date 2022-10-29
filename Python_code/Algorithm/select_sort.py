# coding=GBK
def select_sort(li):
    length_list = len(li)
    for i in range(length_list - 1):
        min_val = i
        for j in range(i + 1, length_list):
            if li[j] < li[min_val]:
                min_val = j
        li[i], li[min_val] = li[min_val], li[i]
    return li


def select_sort2(l1, i):
    if i == 0:
        return l1
    max_j = i
    for j in range(i):
        if l1[j] > l1[max_j]:
            max_j = j
        l1[i], l1[max_j] = l1[max_j], l1[i]
    select_sort2(l1, i - 1)


A = [3, 2, 4, 1, 5, 7, 6]
print(select_sort2(A, 6))
