"""
Find the median of a given integers of array

"""


def findMedian(arr_: list) -> int:
    # Write your code here 
    # The function should return the integer median
    arr_.sort()
    med_ind = int(len(arr_)/2)

    return arr_[med_ind]

arr = [1, 0, 3, 4, 6, 2, 5, 9, 11, 15, 10]

median = findMedian(arr)
print(median)