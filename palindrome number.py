s=0
n=3
cp=n
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
    if cp==s:
        print('Palindrome number')
    else:
            print('not a palindrome')
              
