
startYear = int(input("enter the start year: "))
endYear = int(input("enter the end year: "))
s=[]
b=[]
#loop through between the start and end year
for year in range(startYear, endYear):
  #check if the year is a Leap year if yes print
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    s.append(year)
  else:
    b.append(year)
print("leap years are : ",s)
print("non-leap years are: ",b)
