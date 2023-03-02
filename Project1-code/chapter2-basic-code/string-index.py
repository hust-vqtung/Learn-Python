str = "hello world"
for ch in range(0, len(str)):   #str[0] = "h", str[1] = "e"
    print(str[ch], end=' ')     #str[10] = "d"

print()

for ch in range(0-len(str), 0): #str[-11] = "h", str[-10] = "e"
    print(str[ch], end=' ')     #str[-1] = "d"