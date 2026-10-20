print("AI Code Error Explainer")
print("Project setup complete!")

# TASK 2: Practising error handling

for i in range(3):
    try:
        userInput = int(input("Enter a number to get divided by 100: "))
        divide = 100 / userInput
        print(divide)

    except ValueError as error:
        print(str(error) + ": It was a value error")
    except ZeroDivisionError as error:
        print(str(error) + ":It was a zerodivisionerror. ")


# TASK 4: Basic error explainer

print("\nWelcome to the Error Explainer!")

errorType = input("What type of Python error did you get? ")

if errorType == "ValueError":
    print("This happens when a value is unsuitable for an operation.")

elif errorType == "SyntaxError":
    print("This happens when Python cannot understand the structure of your code.")

elif errorType == "NameError":
    print("This happens when you use a name or variable that Python cannot find.")

else:
    print("Sorry, I don't recognise that error type yet.")
