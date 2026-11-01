age=int(input())
dis=int(input())
if age<12:
  print(int((dis*5)*0.5))
elif 12<=age<=59:
  print(int((dis*5)*1))
else:
  print(int((dis*5)*0.75))
