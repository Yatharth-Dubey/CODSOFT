num = 0
a = int(input("enter the no."))
while a > 0:
    r = a%10
    num = (num*10)+r
    a = a//10
print(num)