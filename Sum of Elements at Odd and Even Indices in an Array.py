n=int(input())
a=list(map(int,input().split()))
esum=osum=0
for i in a:
  if a.index(i)%2==0:
    esum+=i
  else:
    osum+=i
print(esum,osum)
