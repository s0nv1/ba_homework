
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def choose_func(nums: list, func1, func2):
    num_more_zero = lambda x: True if x > 0 else False
    len_nums_more_zero = len(list(filter(num_more_zero, nums)))
    if len(nums) == len_nums_more_zero:
        return square_nums(nums)
    else:
        return remove_negatives(nums)
    
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
