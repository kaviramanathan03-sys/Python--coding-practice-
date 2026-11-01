s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
mark=s1+s2+s3+s4+s5
mark >0 
avg=mark/5
if avg>=90:
  print("Excellent!")
elif 80<=avg<90:
  print("Great Job!")
elif 70<=avg<80:
  print("Good Effort!")
elif 50<=avg<70:
  print("Keep Trying!")
else:
  print("Better Luck Next Time!")
