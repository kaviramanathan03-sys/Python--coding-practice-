n=input()
vow="aeiouAEIOU"
vcount=ccount=0
for i in n:
  if i in vow:
    vcount+=1
  else:
    ccount+=1
print(vcount)
print(ccount)
