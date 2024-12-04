print("ฟอร์มรับข้อมูลระบบยืมคืนอุปกรณ์")

print("\nกรอกข้อมูลตนเองครับ")

room = input("\nชั้น [ม.1/4, ม.2/4, ม.3/4, ม.4/4, ม.5/4, ม.6/4] คือ ")
no = input("\nเลขที่ [พิมพ์ตัวเลขเท่านั้นครับ] ")
nickname = input("\nชื่อเล่น ")
device = input("\nอุปกรณ์ที่ต้องการยืม [Notebook, MacBook, iPad] คือ ")

print("\nสรุปข้อมูล", nickname, " ชั้น ", room, " เลขที่ ", no)
print("ต้องการยืม ", device)