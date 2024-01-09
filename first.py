print ("""
       
        Welcome to calculator!
       Enter the operaiton you want to proceed:
       1) Addition
       2) Subtraction
       3) Division
       4) Multiplication
       5) Exit 


""")


def sum():
    num1, num2 = take_input()
    return (num1 + num2)

def sub():
    num1, num2 = take_input()
    return (num1 - num2)

def div():
    num1, num2 = take_input()
    return (num1 / num2)

def div():
    num1, num2 = take_input()
    return (num1 * num2)

def take_input():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    
    return first_num,second_num

choice = int(input("Enter your choice:"))
    
if choice == 1:
    print("The sum is : ", sum())

elif choice == 2:
    print("The difference is : ", sub())

elif choice == 3:
    print("The result of division is : ", div())

elif choice == 4:
    print("The result of multiplication is : ", div())










