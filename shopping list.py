#shopping list
ls=[ ]
while 1:
    item=input('enter the  name of item')
    if item=="":
            break
    ls.append(item)
ls.sort()
print(ls)
