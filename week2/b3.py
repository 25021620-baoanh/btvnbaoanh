c=input("nhập kí tự: ")
if 'A'<= c <= 'Z': #là chữ hoa
    print("chữ thường tương ứng là:",chr(ord(c)+32))
elif 'a'<= c <= 'z': #là chữ thường
    print("chữ hoa tương ứng là:",chr(ord(c)-32))
else:
    print("không phải kí tự")