number = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n=int(input("enter sum of numbers:"))

pair=[]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if(number[i]+number[j]==n):
            new = (min(number[i],number[j]),max(number[i],number[j]))
            if new not in pair:
                pair.append(new)
print(pair)

