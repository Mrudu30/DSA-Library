# You don't need to read input or print anything. Complete the function searchInSorted() which takes the sorted array arr[], its size N and the element K as input parameters and returns 1 if K is present in the array, else it returns -1.

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        index = -1
        for i in range(len(arr)):
            if arr[i] == K:
                index = 1
                break
        return index