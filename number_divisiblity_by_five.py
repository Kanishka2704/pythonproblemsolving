#display number if Divisible by 5 from list

list1 = [10,20,30,23,24,46,78]
for i in list1:
    if(i%5==0):
        print(i)

list2=[num for num in list1 if(num%5==0)]
print(list2)
