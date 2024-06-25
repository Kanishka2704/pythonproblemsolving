# 1,2,3,4,5,6,7,8,9,10 - 5 even and odd numbers

#if ,for,increment/assignment operator -+=1

list_num =[1,2,3,4,5,6,7,8,9,10]

#initialization
even_count = 0
odd_count = 0

for num in list_num:
    if(num%2==0):
        even_count+=1
    else:
        odd_count+=1
        
print("Number of even numbers:",even_count)
print("Number of odd numbers:",odd_count)

even_num =[num for num in list_num if num%2==0]
odd_num =[num for num in list_num if num%2!=0]
print(len(even_num))
print(len(odd_num))
