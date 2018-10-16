s=input("Enter a String : ")
n=len(s)
c=0
for i in range(0,n):
    if s[i]!=s[(n-1)-i]:
        c+=1
if c==1:
    print("It is not Palindrome")
else:
    print("It is a palindrome")
