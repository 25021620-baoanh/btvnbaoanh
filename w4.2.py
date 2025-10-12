a=int(input("nhập a:"))
if a<=1:
    print("False")
else:
    for i in range(2,(int(a**0.5)+1),1):
        if a%i==0:
            print("False")
            break
    else:
            print("True")


