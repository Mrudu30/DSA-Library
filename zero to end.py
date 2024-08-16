# Problem statement
# Given an array 'arr' of 'n' non-negative integers, your task is to move all the zeros to the end of the array while keeping the non-zero elements at the start of the array in their original order. Return the modified array.

def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    new_array = []
    count = 0
    for i in range(n):
        if a[i] != 0:
            new_array.append(a[i])
        else:
            count += 1
    for i in range(count):
        new_array.append(0)

    return new_array