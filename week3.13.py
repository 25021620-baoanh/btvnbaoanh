a=float(input("nhập a:"))
b=float(input("nhập b:"))
#tìm nghiệm pt ax+b=0
if a==b==0:
    print("vô số nghiệm")
elif a==0 and b!=0:
    print("vô nghiệm")
else:
    print(f"nghiệm duy nhất:{(-b/a):.2f}")