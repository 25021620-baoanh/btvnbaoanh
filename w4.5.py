n=int(input("nhập n:"))
so=[]
for i in range(n):
    x= int(input(f"nhập số thứ {i+1}:"))
    so.append(x)
if 42 in so:
    print("I've found the meaning of life!")
else:
    print("It's a joke")