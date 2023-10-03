#frequency of each char of string

'''
>>>hello
 h:1
 e:1
 l:2
 o:1

>>> banana
 b:1
 a:3
 n:2
'''

st=input('Enter the string')
reg=''
for i in st:
   if i not in reg:
       
        print(f'{i}: {st.count(i)}')
        reg += i
 
