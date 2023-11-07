"""
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    

    k = 0  # Initialize k to 0

    for i in range(len(nums)):
        # Check if the current element is the same as the previous two elements
        if k < 2 or nums[i] != nums[k-1] or nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1

    return k, nums

nums = [0,1,1,2,2,3]
k, new_nums = removeDuplicates(nums)

print(k)
print(len(new_nums))