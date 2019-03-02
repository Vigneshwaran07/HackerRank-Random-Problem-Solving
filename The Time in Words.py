t = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

h = int(input())
m = int(input())

if(m==0):
    print("{} o' clock".format(t[h]))
elif(m==1):
    print("one minute past {}".format(t[h]))
elif(m==59):
    print("one minute to {}".format(t[(h%12)+1]))
elif(m==15):
    print("quarter past {}".format(t[h]))
elif(m==30):
    print("half past {}".format(t[h]))
elif(m==45):
    print("quarter to {}".format(t[(h%12)+1]))
elif(m<=30):
    print("{} minutes past {}".format(t[m],t[h]))
elif(m>30):
    print("{} minutes to {}".format(t[60-m], t[(h%12)+1]))

