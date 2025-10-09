name=input("nhập tên: ")
old=int(input("nhập chỉ số cũ:"))
new=int(input("nhập chỉ số mới:"))
kmh=new-old
if kmh<0:
    print("lỗi")
else:
    if kmh<= 50:
        print(f"số tiền là:{1.08*kmh*1984}","đồng")
    elif 50<kmh<=100:
        print(f"số tiền là:{1.08*(50*1984+(kmh-50)*2050)}",'đồng')
    elif 100<kmh<=200:
        s=50*1984+50*2050+(kmh-100)*2380
        print("số tiền là:",1.08*s,"đồng")
    elif 200<kmh<=300:
        s=50*1984+50*2050+100*2380+(kmh-200)*2998
        print("số tiền là:",1.08*s,'đồng')
    elif 300<kmh<=400:
        s=50*(1984+2050)+100*(2380+2998)+(kmh-300)*3350
        print("số tiền là: ",1.08*s,"đồng")
    else:
        s=50*(1984+2050)+100*(2380+2998+3350)+(kmh-400)*3460
        print("số tiền là:",1.08*s,"đồng")
    