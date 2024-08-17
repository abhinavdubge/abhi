s=input("Enter a string")
p=input("Enter a charecter")
num=0
for i in range(len(s)):
  if s[i]==p:
    num=num+1
print(num,"times",p,"appeared in",s)
