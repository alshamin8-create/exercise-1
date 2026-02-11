
def multiply(a, b):
    return a * b

# def sum(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y


# ##prompt the user for their name
# name = input("enter you name: ")
# #prompt the user for their age
# age = input("Enter your age:")

# print( name  + "'s age is:",age)










# number= int(input("Enter a number" + " "))
# if number %2 == 0:
#     if number %4 ==0:
#         print(" The number is a multiple of 4 ")
#     else:
#         print(" The number is even ")

# else:
#     print(" The number is odd ")
# num= int(input("Enter a number to check "))
# check= int(input("Enter number to check if the previous number devides evenly by it "))
# if num % check ==0:
#     print(" The number divides evenly ")
# else:
#     print(" The number does not divide evenly ")

# #Lara's Code!
# #Function to get a positive integer from the user
# def get_positive_integer(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value <=0:
#                 print("Please enter a positive integer.")
#             else:
#                 return value
#         except ValueError:
#             print("That's not a valid integer, Please enter a valid positive integer.")

# #Ask the user for a positive integer
# n1= get_positive_integer("Enter a valid positive integer:")
# #check if the number is a multiple of 4
# if n1 %4 ==0:
#     print(f"The number {n1} is a multiple of 4.")
# #check if the number is even or odd
# if n1 %2 ==0:
#     print(f"The number {n1} is even.")
# else:
#     print (f"The number{n1} is odd.")
# #Ask the user for 2 positive integers and check if the first number can be evenly divided into the second
# num= get_positive_integer("Enter the first positive integer:")
# check= get_positive_integer("Enter the second positive integer:")
# if num % check ==0:
#     print(f"The number{num} can be evenly divided by{check}.")
# else:
#     print(f"The number {num} cannot be evenly divided by{check}.")







# def first_last_list(prompt):
    
#     while True:
#         try:
#             first_num = int(input(prompt))
#             second_num = int(input(prompt))
#             if first_num != a[0] and second_num != a[4]:
#                 print("you entered a wrong index, try again!")
#             else:
#                 return first_num, second_num
    
#         except IndexError:
#             print("You entered a wrong number")
# a= [0,1,2,3,4,5,6,7,8,9]
# first_num=input("Enter the first number of the list")
# second_num=input("Enter the last number of the list")
# if first_num == a[0]:
#     print("You entered the first number of the list: ", a[0])
# elif second_num == a[4]:
#         print("You entered the last number of the list: ", a[4])
# else:
#         print("You entered a wrong index, try again!")


def new_list(numbers):
     if len(numbers)<3:
          print("The list must be at least 3 numbers long, try again!")
          
     return [numbers[0], numbers[-1]]
a= [1,2,3,4,5,6,7,8,9]
print(new_list(a))


    