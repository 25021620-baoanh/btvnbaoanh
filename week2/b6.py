a=float(input("cạnh thứ nhất:"))
b=float(input("cạnh thứ hai:"))
c=float(input("cạnh thứ ba:"))
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
    print("Đây là 1 tam giác")
    p=(a+b+c)/2
    print(f" diện tích tam giác là:{(p*(p-a)*(p-b)*(p-c))**(0.5):.2f}")
else:
    print("đây không là 3 cạnh tam giác")
