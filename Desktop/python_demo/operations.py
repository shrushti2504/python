numbers = [10,3,6,5,8,5,2,7,9,10]
print(""" select any option : 
    A : print length of list 
    B : display first 3 numbers of list 
    C : print sum of odd numbers in list
    D : print number of duplicate numbers from list
    E : print list without duplicate numbers""")

key = input("enter any key from A to E : ")


if key == "A":
    length = len(numbers)
    print("length of numbers is : " ,length)

elif key == "B":
    display_numbers = numbers[:3]
    print(display_numbers)

elif key == "C":
    sum_of_odds =0 
    for num in numbers:
        if(num % 2 != 0):
            sum_of_odds += num
    print( sum_of_odds)

elif key == "D":
    duplicates = []
    for num in numbers:
        if numbers.count(num)>1 and num not in duplicates:
            duplicates.append(num)
    print(len(duplicates))
    
elif key == "E":
    list1 = []
    for num in numbers:
        count = numbers.count(num)
        if(count == 1):
            list1.append(num)
    print(list1)

else:
    print("please enter key from 1 to 5")








