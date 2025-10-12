n=int(input("nhập n:"))
if 0< n <=1000:
    sum=0
    for i in range(1,n+1):
        sum= sum + i
    print(sum)