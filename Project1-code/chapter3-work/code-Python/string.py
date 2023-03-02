
s = input().upper()
while(s[0]==' '): # s = s.lstrip()
    s = s[1:]
while(s[-1]==' '): # s = s.rstrip()
    s = s[:len(s)-1]
i = 0
while(i<len(s)):
    if(s[i]==' '):
        while(s[i+1]==' '):
            s = s[:i+1] + s[i+2:]
    i += 1
print(s)

# # use reg
# import re
# s = input().strip()
# s = re.sub(' +', ' ', s.upper())
# print(s)