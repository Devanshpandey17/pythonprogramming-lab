# reverse number of given number

num=int(input('enter the number:'))
s=0
while num !=0:
    r= num % 10
    s=s*10+r
    num=num//10

print('reverse number',s)
