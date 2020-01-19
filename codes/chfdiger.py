t = int(input())
while(t > 0):
    t = t - 1
    count = 0
    n, d = input().split(" ")
    s = n
    result = 0
    n = n + d
    length = len(n)
    for i in range(0,length - 1):
        if(n[i] >= n[i + 1]):
            count = count + 1
        else:
            result = 1
            str = str + n[i]
    for i in range(0,count):
        str = str + d
    if(result == 1):
        print(str)
    else:
        print(s)
