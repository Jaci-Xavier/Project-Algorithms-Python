def remove_negative_numbers(list):
    return [num for num in list if isinstance(num, int) and num > 0]


def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    nums = remove_negative_numbers(nums)
    counter = set()

    for num in nums:
        if num in counter:
            return num
        counter.add(num)

    return False
