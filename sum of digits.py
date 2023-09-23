#sum of digits
s=0
n=123
cp=n
while n!=0:
    r=n%10
    s=s+r
    n=n//10
    print(f'sum of digits {cp} is {s}')
    
