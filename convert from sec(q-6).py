sec=int(input("enter the time"))
h=(sec//(60*60))#hours
sec=sec%(60*60)#remaining seconds after hours
m=(sec//60)#minutes
sec=sec%60#remaining seconds aftr minutes
print(f'(h):(min):(sec)')
