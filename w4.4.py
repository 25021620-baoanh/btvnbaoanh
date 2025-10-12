n=int(input("nhập n:"))
count=0
m=abs(n)
if m==0:
    print("có 1 chữ số")
else:
    while m>0 :
        count +=1
        m//=10
print(f"số n có:{count} chữ số")