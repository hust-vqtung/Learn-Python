fb = [0 for i in range(100)]

def memFibo(n):
    if(n<2):
        return n
    else:
        if(fb[n]==0):
            fb[n] = memFibo(n-1) + memFibo(n-2)
        return fb[n]
    
n = int(input())
i = 0
while(memFibo(i)<=n):
    print(memFibo(i), end=' ')
    i += 1
