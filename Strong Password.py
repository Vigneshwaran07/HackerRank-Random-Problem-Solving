def password(n, pswd):
    count = 0    
    if any(i.isdigit() for i in pswd)==False:
        count+=1
    if any(i.islower() for i in pswd)==False:
        count+=1
    if any(i.isupper() for i in pswd)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in pswd)==False:
        count+=1
    return max(count,6-n)
print(password(int(input()), input()))
