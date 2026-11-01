n=input()
a=list(map(int,input().split()))
el=[]
ol=[]
for i in a:
  if i%2==0:
    el.append(i)
  
  else:
    ol.append(i)
if len(el)!=0:
  print(max(el))
else:
  print("None")
if len(ol)!=0:
  print(max(ol))
else:
  print("None")
