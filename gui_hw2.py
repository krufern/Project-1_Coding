from tkinter import *
from tkinter import ttk
import csv

# สร้าง GUI
GUI = Tk()
GUI.geometry('500x600')
GUI.title('โปรแกรมบริการนักเรียน')

# ฟังก์ชันสำหรับบันทึกข้อมูลลง CSV
def writetocsv(data):
    with open('student_services.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

# ฟังก์ชันบันทึกข้อมูล
def Save():
    student_id = v_student_id.get()
    student_name = student_data.get(student_id, "ไม่พบข้อมูล")
    service_choice = v_service.get()
    if student_name == "ไม่พบข้อมูล":
        print(f"ไม่พบข้อมูลสำหรับรหัสนักเรียน {student_id}")
        return

    service_map = {
        "1": "ยืมหนังสือ",
        "2": "คืนหนังสือ",
        "3": "ยืมอุปกรณ์",
        "4": "คืนอุปกรณ์",
        "5": "ปริ้นงาน"
    }
    
    selected_service = service_map.get(service_choice, "บริการไม่ถูกต้อง")
    if selected_service == "บริการไม่ถูกต้อง":
        print("เลือกบริการไม่ถูกต้อง")
        return
    
    data = [student_id, student_name, selected_service]
    writetocsv(data)
    
    v_student_id.set('')
    v_service.set('')
    print(f"บันทึกข้อมูลเรียบร้อย! รหัสนักเรียน: {student_id}, ชื่อ: {student_name}, บริการ: {selected_service}")

# ข้อมูลนักเรียน (จำลอง)
student_data = {
    "12345": "สมชาย",
    "54321": "สมหญิง",
    "11111": "ประเสริฐ",
    "22222": "สมบัติ",
    "33333": "สมจิตร"
}

# ฟอร์มสำหรับกรอกข้อมูล
L = Label(GUI, text='กรอกข้อมูลที่นี่', font=('Angsana New', 25))
L.pack()

L = Label(GUI, text='รหัสนักเรียน (5 หลัก)', font=('Angsana New', 20))
L.pack()
v_student_id = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_student_id, font=('Angsana New', 20))
E1.pack()

L = Label(GUI, text='บริการที่เลือก', font=('Angsana New', 20))
L.pack()
v_service = StringVar()
service_options = ["ยืมหนังสือ", "คืนหนังสือ", "ยืมอุปกรณ์", "คืนอุปกรณ์", "ปริ้นงาน"]
service_menu = ttk.Combobox(GUI, textvariable=v_service, values=service_options, font=('Angsana New', 20))
service_menu.pack()

B1 = ttk.Button(GUI, text='บันทึก', command=Save)
B1.pack(pady=30, ipadx=30, ipady=20)

GUI.mainloop()