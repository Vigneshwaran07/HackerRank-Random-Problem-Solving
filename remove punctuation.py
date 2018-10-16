p= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s=str(input("Enter the String  "))
l=len(s)
j=0
s1=""
for i in range(0,l):
    if s[i] not in p :
        s1+=s[i]
        
print(s1)        
    
