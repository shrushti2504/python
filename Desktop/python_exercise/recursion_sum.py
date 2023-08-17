numbers = [1, 2, 3, 4, 5]

# def sum_recursion(nums, index):
#     if index == 0:
#         return nums[index]
#     else:
#         return nums[index] + sum_recursion(nums, index - 1)
# length =  len(numbers) - 1
# total_sum = sum_recursion(numbers,length)
def sum_recursion(number):
    if len(number)==0:
        return 0
    else:
        return number[0] + sum_recursion(number[1:]) 
ans = sum_recursion([1, 3, 4, 2, 5])
print(ans)