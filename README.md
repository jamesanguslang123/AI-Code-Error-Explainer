# AI-Code-Error-Explainer
Starting out error explanations.
# AI Code Error Explainer

## About the Project
This is a Python project I am developing to help programmers understand errors in their code. The aim is to eventually use AI to explain errors in plain English and suggest possible fixes.

## Current Features

### 1. Basic Error Explainer
- Recognises selected Python error types, including `ValueError`, `SyntaxError`, and `NameError`.
- Displays a basic explanation of each recognised error.
- Provides a message when an error type is not recognised.

### 2. Python Code Checker
- Uses Python's `ast` module to check whether code has valid syntax.
- Uses `exec()` to run code during testing.
- Catches selected runtime errors, including `NameError`, `TypeError`, and `ValueError`.
- Displays error details to help identify what went wrong.

## Technologies Used
- Python
- Python's built-in `ast` module
- Exception handling using `try` and `except`

## What I Have Learned
- How Python handles exceptions.
- How to use `try`, `except`, and error objects.
- The difference between syntax errors and runtime errors.
- How to check Python syntax using `ast.parse()`.
- How to catch and display common runtime errors.

## Future Plans
- Improve error explanations and suggest possible fixes.
- Analyse code to help identify errors automatically.
- Integrate an AI model to explain errors in natural language.
- Develop a user-friendly interface for the tool.
- Add more error types and testing features.

## Current Status
This project is in its early development stage. The current version uses predefined explanations and basic error checking. AI integration has not yet been implemented.

## Important Safety Note
The current code checker uses `exec()` to run submitted Python code. It is intended for controlled testing with trusted code only and is not safe for running arbitrary user-submitted code.
