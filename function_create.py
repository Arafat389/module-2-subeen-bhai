def name():
    print("hello")

name()

def name(n):
    print("hello" , n)
num = "Arafat"
name(num)

def name(n):
    print("hello" , num)
num = input("Enter your name: ")
name(num)

def name(n1 ,n2):
    print("hello" , n1 ,n2)
num1= input("Enter your name: ")
num2= input("Enter your name: ")
name(num1,num2) 

def add(n):
    return n+10
num = 20
result= add(num)
print(result)

def add (p,q):
    return p+q*10
p=3
q=5
result= add(p,q)
print(result)