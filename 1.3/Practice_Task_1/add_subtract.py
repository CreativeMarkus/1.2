num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

operator = input("Enter an operator (+ or -): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

else:
    print("Unknown operator")