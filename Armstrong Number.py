n=int(input())
temp=n
count=0
while n>0:
  n=n//10
  count+=1
n=temp
sum=0
while n>0:
  last=n%10
  sum=sum+last**count
  n=n//10
if(sum==temp):
  print("Armstrong")
else:
  print("Not Armstrong")
