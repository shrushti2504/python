numbers = [1, 2, 3, 4, 5]

def sum_recursion(nums, index):
    if index == 0:
        return nums[index]
    else:
        return nums[index] + sum_recursion(nums, index - 1)
length =  len(numbers) - 1
total_sum = sum_recursion(numbers,length)
print(total_sum)