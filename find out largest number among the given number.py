#find out largest number among the given number
ls=[int(i) for i in input("enter the number: ").split()]
ls2=[ ]
for i in ls:
    if i not in ls2:
        ls2.append(i)
ele=max(ls2)
ls2.remove(ele)
out= max(ls2)
print(out)

    
