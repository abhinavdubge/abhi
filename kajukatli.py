n=int(input("Enter a number"))
for i in range (n):
  a=65
  for j in range(i,n):
    print(" ",end='')
  for m in range(i):
    print(chr(a),end=' ')
    a=a+1
  print()
for i in range (n):
  a=65
  for j in range(i):
    print(" ",end='')
  for m in range(i,n):
    print(chr(a),end=' ')
    a=a+1
  print()
    
    
