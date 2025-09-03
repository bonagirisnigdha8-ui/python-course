num = int(input("Enter the number: "))
t = num
numlen = 0
#ilterate the loop
while t>0:
    numlen = numlen+1
    t = int(t/10)

    if numlen>=4: #condition 1
        numlen = int(numlen/2)
        chk = 0
        while num>0: #ilterate loop
            rem = num%10 
            if chk==numlen: #nested condition 1 
                midOne = rem
            elif chk==(numlen-1):
                midTwo = rem
                num = int(num/10)
                chk = chk+1
                prod =  midOne*midTwo #product of middle digits
                #display the result
                print("Product of Mid digits"(" +str(midOne)+ "*" +str(midTwo+)= prod )