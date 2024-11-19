#Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.

print("select your bike")
print("1. bike")
print("2. car")

c=int(input("enter the transport"))

if (c==1 ):
    print("what type of bike you want")
    print("type 1. sports bike")
    print("type 2. scooty")
    d=int(input("enter the type of bike you want"))
    if d==1:
        print("you have selected sports bike")
    else:
        print('you have selected scooty')

elif c==2:
    print("what type of car do you want")
    print("type 1. sports car")
    print("type 2. track car")
    e=int(input("enter the type of car you want"))
    if e==1:
        print("you have selected sports car")
    else:
        print("you have selected track car")
else:
    print("wrong choice")        