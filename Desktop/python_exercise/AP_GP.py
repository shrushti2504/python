def AP(numbers):
    diff = numbers[1]-numbers[0]
    for i in range(2,len(numbers)):
        if(numbers[i]-numbers[i-1]!=diff):
            wrong = i
            print("wrong term is : ",numbers[i])
            break
    correct = numbers[wrong-1]+diff
    numbers[wrong]=correct
    return numbers
AP_list=[2,5,8,11,15,17]
correct_AP=AP(AP_list)
print(correct_AP)


def GP(number):
    difference=number[1]/number[0]
    for i in range(2,len(number)):
        if(number[i]/number[i-1]!=difference):
            wrong_term = i
            print("wrong term is :",number[i])
            break
    correct_term = number[wrong_term-1]*difference
    number[wrong_term]=correct_term
    return number
GP_list=[3, 9, 27, 81, 244, 729]
correct_GP = GP(GP_list)
print(correct_GP)
