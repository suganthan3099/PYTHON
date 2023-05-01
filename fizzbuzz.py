print("fizzbuzz program")
print('''
1. prints all number divisible by 3 as fizz
2. prints all number divisible by 5 as buzz
3. prints all other number as fizzbuzz \n \n 
you can enter the number to see how many fizz, buss and fizzbuzz are there within the given input\n \n''')
n= int(input("enter the number "))
for num in range(1, n):
    if num % 3 == 0 and num% 5==0:
        print("fizzbuzz")
    elif num % 5 ==0:
        print("buzz")
    elif num % 3==0:
        print("fizz")
    else:
        print(num)