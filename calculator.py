# print("""
#     1. Addition
#     2. Multiply
#     3. Subtract
#     4. Division
#     5. remainder
#     6. power
# """)
# operations_obj = {
#     1: "add",
#     2: "sub",
#     3: "multi",
#     4: "divide",
#     5: "mod",
#     6: "pow"
# }
# print("Choose Operations from 1 to 6: ")
# operation  = int(input())
#
# def perform_math_operation(a,b, opr_name):
#     if opr_name == "add":
#         return a+b
#     elif opr_name == "sub":
#         return a-b
#     elif opr_name == "multi":
#         return a*b
#     elif opr_name =="divide":
#         return a/b
#     elif opr_name == "mod":
#         return a%b
#     elif opr_name == "pow":
#         return a**b
#
# num1  = int(input("Enter value of first number "))
# num2  = int(input("Enter value of second number "))
#
# if operations_obj.get(operation) is None:
#     print("Please Provide valid value from 1 to 6 to perform operations")
# else:
#     print(perform_math_operation(num1, num2, operations_obj.get(operation)))

print("Choose an operation:")
operations_obj = {
    1: ("Addition", lambda a, b: a + b),
    2: ("Multiplication", lambda a, b: a * b),
    3: ("Subtraction", lambda a, b: a - b),
    4: ("Division", lambda a, b: a / b if b != 0 else "Error: Division by zero"),
    5: ("Remainder", lambda a, b: a % b if b != 0 else "Error: Division by zero"),
    6: ("Power", lambda a, b: a ** b)
}

# Display menu dynamically
for key, value in operations_obj.items():
    print(f"{key}. {value[0]}")

# Get user choice
try:
    operation = int(input("Enter your choice (1-6): "))
    if operation not in operations_obj:
        print("Invalid choice. Please choose a number between 1 and 6.")
    else:
        # Get input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform operation
        operation_name, operation_func = operations_obj[operation]
        result = operation_func(num1, num2)
        print(f"Result of {operation_name}: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")