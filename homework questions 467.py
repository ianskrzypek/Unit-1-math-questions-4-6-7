import math

#4)A parcel is thrown downward at a speed of v m/s from an airplane at altitude 11000 m.
#As it falls, its distance from the ground is given by the formula -4.9t2 – vt + 11000, where 
#t is the time in seconds since it was dropped.  Write a program to output the time it will take to reach the ground.
#The input to your program is the positive floating-point number v. The required time is given by the quadratic formula

v4 = float(input("Enter the downward speed (meters/seconds) of the parcel:"))
time4 = (v4 -math.sqrt(v4**2-4*-4.9*11000))/(2*-4.9)
print ("it will take",time4,"seconds for the parcel to reach the ground")

#6) Write a program to calculate the volume and surface area of a cylinder 
#given user input.

radius6 = float(input("enter the radius of your cylinder (in cm):"))
height6 = float(input("enter the height of your cyclinder (in cm):"))
volume6 = math.pi*radius6**2*height6
surface6 = 2*math.pi*radius6**2+math.pi*radius6*2*height6
print ("the volume of your cyclinder (in cm3) is:",volume6)
print ("the surface area of your cylinder (in cm2) is:",surface6)


#7) Write a program that finds and prints all the multiples of a number under 20
num7 = int(input("input a number under 20:"))
for i7 in range (num7,20,num7):
    print (i7)
print ("those are the multiples of",num7,"under 20")