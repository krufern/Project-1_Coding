def convert_number():
    from_base = int(input("กรุณาเลือกฐานของตัวเลขที่ต้องการแปลง (2, 8, 10, 16): "))

    if from_base == 2 or from_base == 8 or from_base == 16:
        num = input(f"กรอกเลขฐาน {from_base}: ")
        decimal_number = int(num, from_base)
        print(f"เลขฐาน {from_base}: {num} -> เลขฐาน 10: {decimal_number}")

    elif from_base == 10:
        num = int(input("กรอกเลขฐาน 10: "))
        print(f"เลขฐาน 10: {num}")
        print(f"เลขฐาน 2: {bin(num)[2:]}")
        print(f"เลขฐาน 8: {oct(num)[2:]}")
        print(f"เลขฐาน 16: {hex(num)[2:].upper()}")

    else:
        print("กรุณากรอกฐานให้ถูกต้อง (2, 8, 10, 16)")

convert_number()
