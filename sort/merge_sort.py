def merge_sort(arr):

    merge_sort.comparisones = 0
    merge_sort.swaps = 0

    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        left_node = arr[:mid]

        # into 2 halves
        right_node = arr[mid:]

        # Sorting the first half
        merge_sort(left_node)

        # Sorting the second half
        merge_sort(right_node)

        i = j = k = 0

        # Copy data to temp arrays left_node[] and right_node[]
        while i < len(left_node) and j < len(right_node):
            if left_node[i] < right_node[j]:
                arr[k] = left_node[i]
                i += 1

                merge_sort.swaps += 1

            else:
                arr[k] = right_node[j]
                j += 1
                merge_sort.swaps += 1
                
            k += 1
            merge_sort.comparisones += 1

        # Checking if any element was left
        while i < len(left_node):
            arr[k] = left_node[i]
            i += 1
            k += 1

            merge_sort.comparisones += 1

        # Checking if any element was right
        while j < len(right_node):
            arr[k] = right_node[j]
            j += 1
            k += 1

            merge_sort.comparisones += 1