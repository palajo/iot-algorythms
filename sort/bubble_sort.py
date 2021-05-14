def bubble_sort(arr):
    n = len(arr)

    bubble_sort.comparisones = 0
    bubble_sort.swaps = 0

    for i in range (n - 1):
        for j in range (0, n - i - 1):
            bubble_sort.comparisones += 1

            if (arr[j] < arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bubble_sort.swaps += 1