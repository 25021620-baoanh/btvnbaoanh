f=input("nhập 1 kí tự:")
if f.isalpha():
    print("kí tự là chữ")
elif f.isdigit():
    print("kí tự là số")
else:
    print("không là chữ và số")