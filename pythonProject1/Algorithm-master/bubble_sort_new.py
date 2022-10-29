def bubble_sort(Arr):
    n = len(Arr)
    flag = 1
    for i in range(n - 1):
        for j in range(1, n - i):
            if Arr[j] < Arr[j - 1]:
                Arr[j], Arr[j - 1] = Arr[j - 1], Arr[j]
                flag = 0
        if flag == 1:
            break


A = [5, 1, 6, 2, 7, 4, 8, 10, 10, 10, 0]
bubble_sort(A)
print(A)
