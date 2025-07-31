#This is a program to simulate projectile motion
import math
j=0
while True:
    if not j==0:
        print("OHH YOU'RE BACK!!...i was eagerly waiting for you to return")
    print("This is a program to simulate motion of a projectile")
    print("The speciality of this program is that you can have your own customised gravity")
    while True:
        try:
            gravity=float(input("Enter the gravity (in m/s^2): "))
            if gravity>0:
                break
            else:
                print("You typed in your love for me didn't you?🥀🥀")
        except ValueError:
            print("Trying to break me??...again??..guess,last time wasn't enough🥀🥀🥀")
            print("You have to type in a real number greater than 0")
    while True:
        try:
            velocity=float(input("Enter the velocity (m/s): "))
            if velocity>0:
                break
            else:
                print("OOPS,you've accidentally typed in your empathy")
                print("Try again")
        except ValueError:
            print("Trying to cheat?...again?...old habits die hard huh🥀🥀")
            print("You have to type in a real number greater than 0")
    while True:
        try:
            print("Angles are counted anticlockwise and angle of projection can't be less than zero or more than 180 as we're considering your height as zero,soo when angle of projection with the ground is zero or 180, it basically means that you're rolling the stone and when the angle exceeds 180,it would mean that you're throwing the stone IN the ground,which is not possible ")
            angle_projectile=float(input("Enter the angle of projection with ground"))
            if angle_projectile>0 and not angle_projectile>=180:
                break
            else:
                print("HMM...you're just as bad at reading words as you're at flirting ")
        except ValueError:
            print("You love playing games don't you?...STOP PLAYING WITH MY FEELINGS!!!..or..uhh MY GPU,YEAH!")
            print("You have to type in a real number greater than 0")
    while True:
        try:
            print("As angles are measured anticlockwise,+ angle for ground basically means an incline looking like '/' this and - angle for ground basically means an incline looking like the former's mirror image,PUT ZERO IF THE GROUND IS HORIZONTAL")
            angle_ground=float(input("Enter the angle of ground with horizontal(if any)"))
            break
        except ValueError:
            print("You were expecting me to break, didn't you?....well I DID!!...You've hurt ME😭😭")
    tof=(2*velocity*(math.sin(angle_projectile*(math.pi/180))))/(gravity*math.cos(angle_ground*(math.pi/180)))
    h_max=(math.pow(velocity*(math.sin(angle_projectile*(math.pi/180))),2))/(2*gravity*math.cos(angle_ground*(math.pi/180)))
    Range=(velocity*math.cos(angle_projectile*(math.pi/180)))*tof-((1/2)*(gravity*math.sin(angle_ground*(math.pi/180)))*(math.pow(tof,2)))
    if not angle_ground%180==90:
        print(f"Time of flight would be {tof} seconds")
        print(f"Maximum Height perpendicular to ground would be {h_max} meters")
        print(f"Range Parallel to the ground would be {Range} meters")
        print("Equation of trajectory of the motion:")
    else:
        print("The ground will literally act as a wall,perpendicular to the ground,there would be no motion")
    if not angle_projectile%180==0 or not angle_ground%180==90:
        print(f"X={velocity*math.cos(angle_projectile*math.pi/180)}*[({math.cos(angle_ground*math.pi/180)})X-({math.sin(angle_ground*math.pi/180)})Y]/{velocity*math.cos((angle_projectile*math.pi/180)+(angle_ground*math.pi/180))}-1/2*{gravity}[({math.cos(angle_ground*math.pi/180)})X-({math.sin(angle_ground*math.pi/180)})Y]/{velocity*math.cos((angle_projectile*math.pi/180)+(angle_ground*math.pi/180))})]²")
    elif angle_ground%180==0:
        print(f"[{math.tan(angle_projectile*math.pi/180)}]*X-(1/2)*{gravity}*X²/[{math.pow(velocity*math.cos(angle_projectile*math.pi/180),2)}]")
    elif angle_ground%180==90:
        print("The incline is literally perpendicular to the ground, like a wall,how will there be any motion?")
    try_again=input("Do you wanna stay??...maybe we can throw some more stones together...type yes if you agree else just press enter")
    if try_again.lower()=="yes":
        j+=1
        continue
    else:
        break
print(f"OH😶....\n....oh🥲\n yeah🙂,guess our journey ends here huh?....NO!, I'M NOT CRYING!!..MY PIXELS ARE SWEATING THOSE AREN'T TEARS!!😭😭😭😭")
print("I hope you remember me when you give inputs to some other program🥀🥀🥀")

