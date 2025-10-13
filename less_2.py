"""
a=int(input())
if a%2==0:
    print("Чётное")
else:
    print("Нечётное")

a=int(input())
z=int(input())
k=int(input())
s=0
while s<k:
    a=a*z
    s=s+1
    print(a*z)

a=int(input())
if a%4==0:
    print("високосный")
else:
    print("не високосный")

a=int(input())
s=0
d=0
f=1
while s<a:
    d=d+f
    s+=1
    f=d
    print(d)

a=int(input())
b=int(input())
if b==0:
    print("делить на 0 нельзя")
elif a%b==0:
    print("a / b = ",a/b,"делится без остатка")
else:
    print("a / b = ",a//b, "остаток", a%b)

for i in range(1,10):
    for j in range(1,10):
        print(f"{i*j}",sep=" ", end=" ")
    print()

a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D>0:
    x1=(D**(1/2)+b)/2*a
    x2=(D**(1/2)-b)/2*a
    print(f"x1={x1} x2={x2}")
elif D==0:
    x=(D**(1/2)+b)/2*a
    print(x)
elif D<0:
    print("нет решений")

a=int(input())
b=int(input())
c=int(input())
if a+b>c or a+c>b or b+c>0:
    if a==b and b==c:
        print("равносторонний")
    elif a==b or a==c or b==c:
        print("равнобедренный")
    else:
        print("разносторонний")
else:
    print("не существует")

a=int(input())
while a>0:
    print(a%10,end="")
    a=a//10

a=int(input())
for i in range(1,a):
    if a%i==0:
        print(f"a = {a/i}*{i}")
"""
a=int(input())
for i in range(1,a):
    s=0
    for n in range(1,i):
        if a%n==0:
            s=s+n
    if s==i:
        print("совершенное")
