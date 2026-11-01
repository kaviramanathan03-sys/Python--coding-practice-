n=input()
vow="aeiouAEIOU"
for i in n:
 if i in vow:
   n=n.replace(i,"")
print(n)
