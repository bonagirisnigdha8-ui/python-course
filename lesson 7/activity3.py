s1 = int(input("enter your first speed: "))
s2 = int(input("enter your second speed: "))
s3 = int(input("enter your third speed: "))

average = (s1 + s2 + s3 )/3
print("the average speed is :  ",average)

if s1<average:
    print("Speed 1 is slower than average with thedifference of ", average-s1)

    if s2<average:
        print("Speed 2 is slower than average with thedifference of ", average-s2)