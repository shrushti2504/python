
string = "PQRQRQRQRQRQRQ"
substring="QRQ"

count=0
start=0
while True:
    index = string.find(substring,start)
    if index == -1:
        break
    count +=1
    start=index+1
print(count)