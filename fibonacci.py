n = int (input("Enter the total number for the series:"))
a=[]
a.append(int(input("Enter the first number:")))
a.append(int(input("Enter the second number:")))
for i in range (2,n):
    a.append(a[i-1]+a[i-2])
print("The fibonacci series is:",a)

    
