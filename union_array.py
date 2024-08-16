def findUnion(self, arr1, arr2, n, m):
    union = []
    i, j = 0, 0

    # Traverse both arrays
    while i < n and j < m:

        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''

        # If the current element of arr1 is smaller, add it
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        # If the current element of arr2 is smaller, add it
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        # If elements are equal, add any one of them and move both pointers
        else:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements of arr1, if any
    while i < n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    # Add remaining elements of arr2, if any
    while j < m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union
