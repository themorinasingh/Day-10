from main import design

print(design)

def calc(a=0):
    if a ==0 :
        a = input("Enter the first number: ")

    operation = input("* \n/ \n+ \n- \nChoose an operation:  ")

    b = input("Enter the second number: ")

    output = ""

    if operation == "*":
        output =  float(a) * float(b)

    elif operation == "/":
        output =  float(a) / float(b)

    elif operation == "+":
        output =  float(a) + float(b)

    elif operation == "-":
        output =  float(a) - float(b)

    result = round(output, 2)

    print(f"Result: {result}")

    continue_operation = input(f"Type y to continue working with {result}, or n to start a new calculation.").lower()

    if continue_operation == "y":
        calc(result)
    elif continue_operation == 'n':
        calc()
    else:
        return


calc()