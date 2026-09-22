# Random Password Generator

## Project Overview

This project is a beginner-level Random Password Generator developed as part of the OIBSIP internship.

The application generates strong random passwords based on user-defined criteria. Users can choose the password length and the types of characters to include.

## Objective

The objective of this project is to build a command-line password generator that:

- Accepts the desired password length
- Enforces a minimum length of 8 characters
- Allows users to select character types
- Generates random passwords based on the selected criteria
- Validates user input
- Allows users to generate multiple passwords without restarting the program

## Technologies Used

- Python
- Random module
- String module

## Features

### Password Length

The user can specify the desired password length. The minimum password length is 8 characters.

### Character Types

The user can choose which character types to include:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

At least two character types must be selected.

### Random Password Generation

The program generates a random password using the selected character types.

### Input Validation

The application validates:

- Password length
- Numeric input
- Minimum password length
- Character-type selection
- Yes/no responses

### Generate Another Password

Users can generate another password without restarting the program.

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Open the Project

Open the `Python-Task3-RandomPasswordGenerator` folder in VS Code.

### 3. Run the Program

Click **Run Python File** in VS Code.

The program will ask for the password length and character types.

## Example

```text
===== Random Password Generator =====

Do you want to generate a password? yes/no: yes

Enter password length (minimum 8): 10

Include uppercase letters? yes/no: yes
Include lowercase letters? yes/no: yes
Include numbers? yes/no: yes
Include symbols? yes/no: yes

Generated password: A7@kp2!Qx9