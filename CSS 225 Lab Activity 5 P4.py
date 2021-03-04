#Miguel Rodriguez
#February 25,2021
#Lab Activity 5 Problem 4

#Write a program that uses a for loop to loop through the numbers 1 to 50.
   # • If the number is a multiple of 3, print “Divisible by three”.
    #• If the number is a multiple of 5 print “Divisible by five”.
    #• If the number is divisible by both 3 and 5, print "Divisible by both".
    #• Otherwise, print the number.
for i in range(1,51):
    if i % 3==0 and i % 5 ==0:
        print("Divisible by both")
    elif i % 3==0:
        print("Divisible by three")
    elif i % 5==0:
        print("Divisible by five")
    else:
        print(i)


