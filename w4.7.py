n=int(input("nhập n:"))
uoc=2
while n>1:
    if n % uoc ==0:
        n //= uoc
    else:
        uoc +=1
print(f"ước số nguyên tố lớn nhất là:{uoc}")