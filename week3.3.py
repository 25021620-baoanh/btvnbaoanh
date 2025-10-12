n=int(input("nhập 1 số:"))
if n>0 and (n & (n-1))==0:
    print(n,"là lũy thừa của 2")
else:
    print(n,"không là lũy thừa của 2")