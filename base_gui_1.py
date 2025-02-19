import tkinter as tk
from tkinter import messagebox

def convert_number():
    try:
        from_base = int(base_var.get())
        num = entry_num.get().strip()
        
        if from_base not in [2, 8, 10, 16]:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาเลือกฐานให้ถูกต้อง (2, 8, 10, 16)")
            return
        
        if from_base == 10:
            decimal_number = int(num)
        else:
            decimal_number = int(num, from_base)
        
        result_var.set(f"เลขฐาน {from_base}: {num}\n"
                       f"เลขฐาน 10: {decimal_number}\n"
                       f"เลขฐาน 2: {bin(decimal_number)[2:]}\n"
                       f"เลขฐาน 8: {oct(decimal_number)[2:]}\n"
                       f"เลขฐาน 16: {hex(decimal_number)[2:].upper()}")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกค่าที่ถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ตัวแปลงเลขฐาน")
root.geometry("400x300")

# เลือกฐานของตัวเลข
base_var = tk.StringVar(value="10")
base_label = tk.Label(root, text="เลือกฐานของเลข: ")
base_label.pack()
base_options = tk.OptionMenu(root, base_var, "2", "8", "10", "16")
base_options.pack()

# กรอกค่าตัวเลข
entry_num = tk.Entry(root)
entry_num.pack()

# ปุ่มแปลงค่า
convert_button = tk.Button(root, text="แปลงค่า", command=convert_number)
convert_button.pack()

# แสดงผลลัพธ์
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, justify="left")
result_label.pack()

# เริ่มโปรแกรม
root.mainloop()
