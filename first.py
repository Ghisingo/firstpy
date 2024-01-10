print ("""
       
       Welcome to calculator!
       Enter the operaiton you want to proceed:
       1) Addition
       2) Subtraction
       3) Division
       4) Multiplication
       5) Exit 


""")

def take_input():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    
    return first_num,second_num

def sum():
    num1, num2 = take_input()
    return (num1 + num2)

def sub():
    num1, num2 = take_input()
    return (num1 - num2)

def div():
    num1, num2 = take_input()
    return (num1 / num2)

def mul():
    num1, num2 = take_input()
    return (num1 * num2)

choice = int(input("Enter your choice:"))
    
if choice == 1:
    print("The sum is : ", sum())

elif choice == 2:
    print("The difference is : ", sub())

elif choice == 3:
    print("The result of division is : ", div())

elif choice == 4:
    print("The result of multiplication is : ", mul())

elif choice == 5:
    print ("Thank you!")
    exit()

else:
    print("choose form 1 to 4")


# again = input(print ("Again? y or n: "))
# y = 1
# n = 0 
# if again == y:
#     print ("""
#        Enter the operaiton you want to proceed:
#        1) Addition
#        2) Subtraction
#        3) Division
#        4) Multiplication
#        5) Exit 
# """, take_input())

# else:
#     print("ok bye")












