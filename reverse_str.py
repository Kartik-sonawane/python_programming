
def reverse(string):
    rev_str=""
    for i in string:
        rev_str= i + rev_str
    print("reverse string is: ", rev_str)

str = input("enter the string :")
print("entered string is: " ,str)
reverse(str)

'''
str = input("enter the string: ")
rev_str = str[::-1]
print(rev_str)
'''