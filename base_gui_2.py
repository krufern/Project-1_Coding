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

def clear_fields():
    entry_num.delete(0, tk.END)
    result_var.set("")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("ตัวแปลงเลขฐาน")
root.geometry("450x350")
root.configure(bg="#f0f0f0")

# เมนูบาร์
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="ออก", command=root.quit)
menu_bar.add_cascade(label="ไฟล์", menu=file_menu)
root.config(menu=menu_bar)

# เลือกฐานของตัวเลข
base_var = tk.StringVar(value="10")
base_label = tk.Label(root, text="เลือกฐานของเลข: ", font=("Arial", 12), bg="#f0f0f0")
base_label.pack(pady=5)
base_options = tk.OptionMenu(root, base_var, "2", "8", "10", "16")
base_options.pack(pady=5)

# กรอกค่าตัวเลข
entry_num = tk.Entry(root, font=("Arial", 12), width=20)
entry_num.pack(pady=5)

# ปุ่มแปลงค่า
convert_button = tk.Button(root, text="แปลงค่า", font=("Arial", 12), command=convert_number, bg="#4CAF50", fg="white")
convert_button.pack(pady=5)

# ปุ่มเคลียร์ข้อมูล
clear_button = tk.Button(root, text="เคลียร์", font=("Arial", 12), command=clear_fields, bg="#f44336", fg="white")
clear_button.pack(pady=5)

# แสดงผลลัพธ์
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), bg="#f0f0f0", justify="left")
result_label.pack(pady=10)

# เริ่มโปรแกรม
root.mainloop()
