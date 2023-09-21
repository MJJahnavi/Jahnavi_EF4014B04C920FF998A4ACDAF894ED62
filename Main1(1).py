def isleapyear(year):
  if(year%4==0) and (year%100==0) or (year400==0):
    return True
  else:
    return False
year=int(input("Enter the year:"))
if isleapyear(year):
  print("The year is a leapyear!")
else:
  print("The year is not a leapyear!")
