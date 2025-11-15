def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate numbers for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


# ---------- Example Input ----------
nums = [-1, 0, 1, 2, -1, -4]

# ---------- Function Call ----------
output = three_sum(nums)

# ---------- Display Output ----------
print("All unique triplets with sum 0 are:")
print(output)
