import tkinter as tk
from tkinter import ttk

def convert_base():
    input_num = entry_input.get()
    from_base = int(combo_from_base.get())
    to_base = int(combo_to_base.get())
    
    try:
        # แปลงเป็นฐาน 10 ก่อน
        num_in_base10 = int(input_num, from_base)
        # แปลงเป็นฐานปลายทาง
        if to_base == 2:
            result = bin(num_in_base10)[2:]
        elif to_base == 8:
            result = oct(num_in_base10)[2:]
        elif to_base == 16:
            result = hex(num_in_base10)[2:].upper()
        else:
            result = str(num_in_base10)
        
        label_result.config(text=f"ผลลัพธ์: {result}")
    except ValueError:
        label_result.config(text="ข้อผิดพลาด: กรุณากรอกตัวเลขที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมแปลงเลขฐาน")

# Input
tk.Label(root, text="กรอกตัวเลข:").grid(row=0, column=0, padx=10, pady=10)
entry_input = tk.Entry(root)
entry_input.grid(row=0, column=1, padx=10, pady=10)

# From Base
tk.Label(root, text="จากฐาน:").grid(row=1, column=0, padx=10, pady=10)
combo_from_base = ttk.Combobox(root, values=[2, 8, 10, 16])
combo_from_base.set(10)
combo_from_base.grid(row=1, column=1, padx=10, pady=10)

# To Base
tk.Label(root, text="แปลงเป็นฐาน:").grid(row=2, column=0, padx=10, pady=10)
combo_to_base = ttk.Combobox(root, values=[2, 8, 10, 16])
combo_to_base.set(2)
combo_to_base.grid(row=2, column=1, padx=10, pady=10)

# Convert Button
btn_convert = tk.Button(root, text="แปลง", command=convert_base)
btn_convert.grid(row=3, column=0, columnspan=2, pady=20)

# Result
label_result = tk.Label(root, text="ผลลัพธ์: ", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# เริ่มต้นโปรแกรม
root.mainloop()
