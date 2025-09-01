def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        else:  # result == "right"
            low = mid + 1
    return -1


def firstposition(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"   # keep going left
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def lastposition(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "right"  # keep going right
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def first_last(nums, target):
    n = firstposition(nums, target), lastposition(nums, target)
    print(n)


# -------------------
nums = [5, 7, 7, 8, 8, 10]
target = 8
first_last(nums, target)
