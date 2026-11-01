a=input().lower().replace(" ","").strip()
b=input().lower().replace(" ","").strip()
if sorted(a)==sorted(b):
  print("true")
else:
  print("false")
