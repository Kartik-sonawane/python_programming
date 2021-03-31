number = int(input("Enter the number: "))
rev_number = 0
sum = 0

#main logic
while (number > 0):
    remainder = number % 10
    rev_number = (rev_number * 10) + remainder
    sum = sum + remainder                        # sum of digits
    number = number // 10

#printing 
print("The reverse number is :",rev_number)
print("the sum is :", sum)
