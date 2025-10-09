A=input("nhập chữ hoa: ")
if A=='A':
    print(" không hợp lệ")
elif A<='A' or A>='z':
    print(" không tồn tại")
else:
    print("chữ thg liền trước:",chr(ord(A)+31))