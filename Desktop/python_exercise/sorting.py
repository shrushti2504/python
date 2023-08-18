def sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
               #swap
                num[j], num[j + 1] = num[j + 1], num[j]

number = [1, 5, 7, 3, 9, 2]
sort(number)
for k in range(len(number)):
    print(number[k])

   