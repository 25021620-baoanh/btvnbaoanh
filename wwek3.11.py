a=int(input("nhập a:"))
b=int(input("nhập b:"))
c=int(input("nhập c:"))
if a+b<=c or a+c<=b or b+c<=a:
    print("không là tam giác")
elif a==c==b:
    print("tam giác đều")
elif a==b or a==c or b==c:
    print("tam giác cân")
else:
    print("tam giác thường")