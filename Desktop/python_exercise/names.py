names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
length_5 = []
length_6=[]
length_8 = []

print("the most frequent name length is : ")
for name in names:
    if(len(name) == 5):
        length_5.append(name)
    elif(len(name) == 6):
        length_6.append(name)
    elif(len(name) == 8):
        length_8.append(name)
print(length_5)
print(length_6)
print(length_8)
length_7 = []


print("the least frequent length name is : ")
for name in names:
    if(len(name) == 7):
        length_7.append(name)
    
print(length_7)
print(length_8)
print(length_6)
