import ast

print("Python Code Error Checker")

userCode = input("Enter Python code: ")

try:
    ast.parse(userCode)
    print("Syntax is valid!")

    try:
        exec(userCode)
        print("Code ran successfully!")

    except NameError as error:
        print("NameError detected!")
        print("Details:", error)

    except TypeError as error:
        print("TypeError detected!")
        print("Details:", error)

    except ValueError as error:
        print("ValueError detected!")
        print("Details:", error)

except SyntaxError as error:
    print("SyntaxError detected!")
    print("Details:", error)