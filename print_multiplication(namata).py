print("5x1=5")
print("5x2=10")
print("5x3=15")
print("5x4=20")
print("5x5=25")
print("5x6=30")
print("5x7=35")
print("5x8=40")
print("5x9=45")
print("5x10=50")



print("5x1=",5*1)
print("5x2=",5*2)
print("5x3=",5*3)
print("5x4=",5*4)
print("5x5=",5*5)
print("5x6=",5*6)
print("5x7=",5*7)
print("5x8=",5*8)
print("5x9=",5*9)
print("5x10=",5*10)


#use fpr loop

for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11):
    print("5 x",i, "=",5*i)

n = int(input("enter number: "))   
for i in range(1,11):
    print(n,"x",i, "=",n*i) 

def print_multiplication_table():
    for i in range (1,11):
        print(n,"x",i,"=",n*i)
n= int(input("enter number: "))            
print_multiplication_table()