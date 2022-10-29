def bubble_sort(Arr):
    for i in range(len(Arr) - 1):
        print(i)
        for j in range(len(Arr) - 1, i, -1):
            k = j - 1
            if Arr[j] < Arr[k]:
                Arr[j - 1], Arr[j] = Arr[j], Arr[j - 1]


A = [8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(A)
print(A)
