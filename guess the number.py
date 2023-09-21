from random import *
c_num=randrange(1,101)
u_num=int(input("guess any number"))
while 1:
       user1=("chance for user1 to guess number")
       user2=("chance for user2 to guess number")
 
       if u_num == c_num:
           print('user1 win ')
           break
       elif u_num>c_num:
           print('Too Large')
       else:
           print('Too small')
