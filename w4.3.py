n=int(input("nhập n:"))
if 0< n <=100:
    gt=1
    for i in range(1,n+1):
        gt *= i
    print(f"n!={gt}")
else:
    print("false")