#Sample Calculator

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "Cannnot divide by 0!!"
    return x/y

def pow(x,y):
    return x**y

def mod(x, y):
    if y == 0:
        return "Cannot perform modulus with 0!!"
    return x % y

print("Select Operation::")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Mod")

choose=input("Enter the Operation:(1,2,3,4,5,6)")

x=float(input("Enter the first numbers:"))
y=float(input("Enter the second numbers:"))

if choose=="1":
    print(add(x,y))
elif choose=="2":
    print(sub(x,y))
elif choose=="3":
    print(mul(x,y))
elif choose=="4":
    print(div(x,y))
elif choose=="5":
    print(pow(x,y))
elif choose=="6":
    print(mod(x,y))
else:
    print("Invalid input")



