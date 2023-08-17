numbers = [1, 2, 3, 4, 5]

def sum_recursion(number):
    if len(number)==0:
        return 0
    else:
        return number[0] + sum_recursion(number[1:]) 
ans = sum_recursion([1, 3, 4, 2, 5])
print(ans)