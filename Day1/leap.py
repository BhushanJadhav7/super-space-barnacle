
year = int(input("Enter year: "))
#all leap year are divisible by 4 whereas for end of century leap year are divisible by 400
if (year%4==0 or year%400==0):
    print(str(year)+" is a Leap Year")

else:
    print(str(year)+" is not a leap Year")


