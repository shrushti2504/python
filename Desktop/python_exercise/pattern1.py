n=int(input("enter numbers for patterns : "))
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            if((i==0 and j==(n-1)/2)or (i==n-1 and j==(n-1)/2) or (j==0 and i==(n-1)/2)or(j==n-1 and i==(n-1)/2)):
                print("  ",end="")
            else:
                print("* ",end="")
        else:
            print("  ",end="")
    print("\n")