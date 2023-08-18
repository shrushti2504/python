import re
emails = ["abc@gmail.com", "123$tt*@xyz.com","good@bad@uk.in","nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
emails2 = []
for i in emails:
    expression = r'^[\w\.-]+@+[\w\.-]+\.[a-zA-Z]{2,3}+$'
    ans = re.match(expression,i)
    if ans:
        emails2.append(i)
print(emails2)
