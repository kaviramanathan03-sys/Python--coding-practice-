n=input()#R2d2
alphacount=numcount=0
for i in n:
  if i.isalpha():
    alphacount+=1
  elif i.isdigit():
    numcount+=1
  if alphacount>0 and numcount>0:
    break
if alphacount>0 and numcount>0:
  print("true")
else:
  print("false")
