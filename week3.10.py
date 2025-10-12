a=int(input("nhập a:"))
b=int(input("nhập b:"))
c=int(input("nhập c:"))
d=int(input("nhập d:"))
if a>=b and a>=c and a>=d:
    print(a,"là số lớn nhất")
elif b>=c and b>=d:
    print(b,"là số lớn nhất")
elif c>=d:
    print(c,"là số lớn nhất")
else:
    print(d,"là số lớn nhất")