def select_sort(array):
    for i in range(len(array)):
        x = i       # min index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
                array[i], array[x] = array[x], array[i]
    return array


A = list(map(int, input().split(',')))
print(select_sort(A))