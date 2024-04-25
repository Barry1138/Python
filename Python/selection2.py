def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

list = [ 5, 3, 1, 2, 6, 4 ]
selection_sort(list)
print("Sorted array")
print(list)
