row = int(input("Enter the number of rows: "))
if row %2==0 :
    half = int(row/2)
else:
    half = int(row/2)+1
space = half-1
for i in range (1,half+1):    
   for j in range (1,space+1):
       print(end = " ") 
    space = space-1
   num = 1
   for j in range (2*i-1):
       print(end = str(num) )
       num = num+1
       print()
       space = 1
       for i in range(1, space+1)
       num = 1
       for j in range(1,2*(half-i)):
           print(end=str(num))
           num = num+1
           print()