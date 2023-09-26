#Password Validation
import time
passwrd='devansh2910'
attempt=3
while True:
    user_pass = input('\nEnter the password')
    if user_pass == passwrd:
        print('Login Succesfull')
        break
    else:
        print('wrong Password,Try Again')

    attempt-=1 
    if attempt <= 0:
        print('failed to login')
        print('waiting time start')
        count=10
        while count:
             time.sleep(1)
             print(count,end='')
             count -= 1
        attempt = 3
