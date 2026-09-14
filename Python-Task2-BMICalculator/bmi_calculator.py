import tkinter as tk
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Create the database
connection = sqlite3.connect("bmi_records.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        bmi REAL NOT NULL,
        category TEXT NOT NULL,
        date_time TEXT NOT NULL
    )
""")

connection.commit()


# Create the main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x450")


# Name
name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()


# Weight
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()


# Height
height_label = tk.Label(window, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()


# Result
result_label = tk.Label(window, text="")
result_label.pack()


# Function to calculate BMI
def calculate_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            result_label.config(text="Please enter your name.")
            return

        if weight <= 0 or height <= 0:
            result_label.config(
                text="Please enter positive values."
            )
            return

        bmi = weight / (height ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            result_color = "blue"
        elif bmi < 25:
            category = "Normal"
            result_color = "green"
        elif bmi < 30:
            category = "Overweight"
            result_color = "orange"
        else:
            category = "Obese"
            result_color = "red"

        # Save record
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO bmi_records
            (name, weight, height, bmi, category, date_time)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, weight, height, bmi, category, date_time))

        connection.commit()

        # Display result with colour
        result_label.config(
            text=f"BMI: {bmi:.2f}\n"
                 f"Category: {category}\n"
                 f"Record saved!",
            fg=result_color
        )

    except ValueError:
        result_label.config(
            text="Please enter numbers for weight and height."
        )

    except sqlite3.Error:
        result_label.config(
            text="Database error. Could not save the record."
        )

# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi
)

calculate_button.pack()


# Function to view BMI history
def view_history():
    history_window = tk.Toplevel(window)
    history_window.title("BMI History")
    history_window.geometry("600x400")

    history_label = tk.Label(
        history_window,
        text="BMI History",
        font=("Arial", 16, "bold")
    )
    history_label.pack()


    cursor.execute("""
        SELECT name, weight, height, bmi, category, date_time
        FROM bmi_records
        ORDER BY date_time DESC
    """)

    records = cursor.fetchall()

    if not records:
        tk.Label(
            history_window,
            text="No BMI records found."
        ).pack()
        return

    for record in records:
        name, weight, height, bmi, category, date_time = record

        record_text = (
            f"Name: {name} | "
            f"Weight: {weight} kg | "
            f"Height: {height} m | "
            f"BMI: {bmi:.2f} | "
            f"{category} | "
            f"{date_time}"
        )

        tk.Label(
            history_window,
            text=record_text,
            anchor="w"
        ).pack(fill="x", padx=10, pady=3)


# View history button
# Function to show BMI trend
def show_bmi_trend():
    name = name_entry.get().strip()

    if not name:
        result_label.config(text="Please enter a name first.")
        return

    cursor.execute("""
        SELECT date_time, bmi
        FROM bmi_records
        WHERE name = ?
        ORDER BY date_time
    """, (name,))

    records = cursor.fetchall()

    if not records:
        result_label.config(text=f"No records found for {name}.")
        return

    dates = [record[0] for record in records]
    bmi_values = [record[1] for record in records]

    graph_window = tk.Toplevel(window)
    graph_window.title(f"BMI Trend - {name}")
    graph_window.geometry("700x500")

    figure, axis = plt.subplots(figsize=(7, 4))

    axis.plot(dates, bmi_values, marker="o")

    axis.set_title(f"BMI Trend for {name}")
    axis.set_xlabel("Date and Time")
    axis.set_ylabel("BMI")

    axis.tick_params(axis="x", rotation=45)

    figure.tight_layout()

    canvas = FigureCanvasTkAgg(
        figure,
        master=graph_window
    )

    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


# View history button
history_button = tk.Button(
    window,
    text="View History",
    command=view_history
)

history_button.pack()
# BMI trend button
trend_button = tk.Button(
    window,
    text="Show BMI Trend",
    command=show_bmi_trend
)

trend_button.pack()


# Start the application
window.mainloop()