# BMI Calculator

## Project Overview

This project is an advanced Python BMI Calculator developed as part of the OIBSIP internship.

The application provides a graphical user interface using Tkinter. It calculates Body Mass Index (BMI), classifies the result into standard health categories, stores user records in an SQLite database, and displays BMI trends using Matplotlib.

## Objective

The objective of this project is to build a BMI calculator that:

- Calculates BMI from weight and height
- Classifies BMI into standard categories
- Validates user input
- Supports multiple named users
- Stores historical BMI records
- Displays BMI trends over time

## Technologies Used

- Python
- Tkinter
- SQLite3
- Matplotlib

## Features

### BMI Calculation

The application calculates BMI using:

BMI = weight / (height²)

Weight is entered in kilograms (kg), and height is entered in meters (m).

### BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| 30 or above | Obese |

### Input Validation

The application handles:

- Non-numeric weight and height
- Negative values
- Empty user name
- Invalid input
- Database errors

### Multi-User Support

Users can enter different names and save BMI records separately.

### SQLite Database

BMI records are stored in:

`bmi_records.db`

Each record contains:

- Name
- Weight
- Height
- BMI
- Category
- Date and time

### BMI History

The application provides a **View History** option to display previously saved BMI records.

### BMI Trend Graph

The **Show BMI Trend** option displays a line graph of a user's BMI values over time using Matplotlib.

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Matplotlib

Open the terminal and run:

```bash
python -m pip install matplotlib


## Project Structure

Python-Task2-BMICalculator/
├── bmi_calculator.py
├── bmi_records.db
├── README.md
└── screenshots/
    ├── bmi_normal_result.png
    ├── bmi_validation.png
    ├── bmi_history.png
    └── bmi_trend.png
