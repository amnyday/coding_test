str = input()
str_p = ''

for s in str: 
    if s.isupper() :
        str_p += s.lower()
    elif s.islower() :
        str_p += s.upper()
print(str_p)