s =set("qwertyuiopasdfghjklzxcvbnm")
a = input().lower()
if (set(a).intersection(s)==s):
    print("pangram")
else:
    print("not pangram")
