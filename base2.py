import tkinter as tk
from tkinter import ttk, messagebox

def validate_input(input_num, base):
    """Validate the input based on the selected base."""
    if base == 2:
        return all(char in '01' for char in input_num)
    elif base == 8:
        return all(char in '01234567' for char in input_num)
    elif base == 10:
        return input_num.isdigit()
    elif base == 16:
        return all(char in '0123456789ABCDEFabcdef' for char in input_num)
    return False

def convert_all_bases():
    input_num = entry_input.get()
    from_base = int(combo_from_base.get())

    if not validate_input(input_num, from_base):
        messagebox.showerror("Error", f"Invalid number for base {from_base}.")
        return

    try:
        # Convert to base 10 first
        num_in_base10 = int(input_num, from_base)
        # Convert to all bases
        bin_result = bin(num_in_base10)[2:]
        oct_result = oct(num_in_base10)[2:]
        dec_result = str(num_in_base10)
        hex_result = hex(num_in_base10)[2:].upper()

        # Update results
        label_bin_result.config(text=f"Base 2: {bin_result}")
        label_oct_result.config(text=f"Base 8: {oct_result}")
        label_dec_result.config(text=f"Base 10: {dec_result}")
        label_hex_result.config(text=f"Base 16: {hex_result}")
    except ValueError:
        messagebox.showerror("Error", "Conversion failed. Please check your input.")

def copy_to_clipboard(result):
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()  # Now it stays on the clipboard
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Base Conversion Tool")
root.geometry("400x400")
root.configure(bg="#f0f4f7")

# Input
tk.Label(root, text="Enter number:", bg="#f0f4f7", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_input = tk.Entry(root, font=("Arial", 12))
entry_input.grid(row=0, column=1, padx=10, pady=10)

# From Base
tk.Label(root, text="From Base:", bg="#f0f4f7", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
combo_from_base = ttk.Combobox(root, values=[2, 8, 10, 16], font=("Arial", 12))
combo_from_base.set(10)
combo_from_base.grid(row=1, column=1, padx=10, pady=10)

# Convert Button
tk.Button(root, text="Convert", font=("Arial", 12), bg="#0078D7", fg="white", command=convert_all_bases).grid(row=2, column=0, columnspan=2, pady=20)

# Results
label_bin_result = tk.Label(root, text="Base 2: ", bg="#f0f4f7", font=("Arial", 12))
label_bin_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

label_oct_result = tk.Label(root, text="Base 8: ", bg="#f0f4f7", font=("Arial", 12))
label_oct_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

label_dec_result = tk.Label(root, text="Base 10: ", bg="#f0f4f7", font=("Arial", 12))
label_dec_result.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

label_hex_result = tk.Label(root, text="Base 16: ", bg="#f0f4f7", font=("Arial", 12))
label_hex_result.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Copy Buttons
tk.Button(root, text="Copy Base 2", font=("Arial", 10), bg="#34A853", fg="white", command=lambda: copy_to_clipboard(label_bin_result.cget("text").split(": ")[1])).grid(row=3, column=2, padx=5)
tk.Button(root, text="Copy Base 8", font=("Arial", 10), bg="#34A853", fg="white", command=lambda: copy_to_clipboard(label_oct_result.cget("text").split(": ")[1])).grid(row=4, column=2, padx=5)
tk.Button(root, text="Copy Base 10", font=("Arial", 10), bg="#34A853", fg="white", command=lambda: copy_to_clipboard(label_dec_result.cget("text").split(": ")[1])).grid(row=5, column=2, padx=5)
tk.Button(root, text="Copy Base 16", font=("Arial", 10), bg="#34A853", fg="white", command=lambda: copy_to_clipboard(label_hex_result.cget("text").split(": ")[1])).grid(row=6, column=2, padx=5)

# Start the program
root.mainloop()
