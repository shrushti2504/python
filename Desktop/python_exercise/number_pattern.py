n=int(input("enter number for pattern : "))
num = 1
for i in range(1,n):
    for j in range(1,i+1):
        print(num,end="")
        num +=1
    print("\n")