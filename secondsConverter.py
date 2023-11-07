"""
QUESTION 1 [TOTAL MARKS: 25]
Write a program that asks the user to enter a number of seconds and works as follows: 
•There are 60 seconds in a minute. If the number of seconds entered by the user
     is greater than or equal to 60, the program should display the number 
    of minutes in that many seconds. 
•There are 3,600 seconds in an hour. If the number of seconds entered by the user is
    greater than or equal to 3,600, the program should display the number of hours in
    that many seconds. 
•There are 86,400 seconds in a day. If the number of seconds entered by the 
user is greater than or equal to 86,400, the program should display the number of days in
that many seconds.

"""

seconds = int(input("Enter a number of seconds: \t"))

if seconds >= 60 and seconds < 3600:
    min = seconds // 60
    secsRemain = seconds % 60

    print("{} minute/s and {} seconds".format(min, secsRemain))

elif seconds >= 3600 and seconds < 86400:
    hour = seconds // 3600
    minsRemain = seconds % 3600

    if minsRemain >=60:
        min = minsRemain // 60
        secsRemain = minsRemain % 60

        print("{} Hours , {} minute/s , {} seconds".format(hour, min, secsRemain))
    else:
        print("{} Hours , {} seconds".format(hour, minsRemain))

elif seconds >= 86400:
    day = seconds // 86400
    hourRemain = seconds % 86400

    if hourRemain >= 3600:
        hour = hourRemain // 3600
        minsRemain = hourRemain % 3600

        if minsRemain >= 60:
            min = minsRemain // 60
            secsRemain = minsRemain % 60

            print("{} Day/s, {} Hour/s , {} minute/s , {} seconds".format(day, hour, min, secsRemain))
        
        else:
            print("{} Day/s, {} Hour/s , {} minute/s , {} seconds".format(day, hour, 0, minsRemain))
   
    else:
        min = hourRemain // 60
        secsRemain = hourRemain % 60

        print("{} Day/s, {} Hour/s , {} minute/s , {} seconds".format(day, 0, min, secsRemain))


