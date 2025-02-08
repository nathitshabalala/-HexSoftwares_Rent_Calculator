import tkinter as tk
from tkinter import messagebox

# Method for getting inputs and calculating the rent
def cal_rent():
    try:
        rent_per_month = float(rent_per_month_entry.get())
        num_months = int(num_months_entry.get())

        # Input validation
        if rent_per_month <= 0:
            messagebox.showerror("Invalid Input", "Rent per month must be greater than 0.")
            return
        if num_months < 1:
            messagebox.showerror("Invalid Input", "Number of months must be at least 1.")
            return

        # Calculate total rent
        total_rent = rent_per_month * num_months
        total_rent_label.config(text=f"Total Rent: R {total_rent:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Invalid input.")

# Method for clearing the inputs and the result
def clear_fields():
    rent_per_month_entry.delete(0, tk.END)
    num_months_entry.delete(0, tk.END)
    total_rent_label.config(text="")

# User Interface
root = tk.Tk()
root.title("Rent Calculator")
root.geometry("400x200")

# Rent input frame
rent_frame = tk.Frame(root)
rent_frame.pack(pady=5)
tk.Label(rent_frame, text="Monthly Rent (R): ").pack(side=tk.LEFT)
rent_per_month_entry = tk.Entry(rent_frame)
rent_per_month_entry.pack(side=tk.LEFT)

# Months input frame
months_frame = tk.Frame(root)
months_frame.pack(pady=5)
tk.Label(months_frame, text="Number of Months: ").pack(side=tk.LEFT)
num_months_entry = tk.Entry(months_frame)
num_months_entry.pack(side=tk.LEFT)

# Buttons frame
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=5)

# Calculate button
calculate_btn = tk.Button(buttons_frame, text="Calculate", command=cal_rent)
calculate_btn.pack(side=tk.LEFT, padx=5)

# Clear button
clear_button = tk.Button(buttons_frame, text="Clear", command=clear_fields)
clear_button.pack(side=tk.LEFT, padx=5)

# Total rent label
total_rent_label = tk.Label(root, text="")
total_rent_label.pack(pady=5)

# Run the application
root.mainloop()
