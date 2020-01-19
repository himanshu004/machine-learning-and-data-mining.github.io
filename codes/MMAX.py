t = int(input())
while(t > 0):
    t = t - 1
    n = int(input())
    k = int(input())
    if(k % n == 0):
        print(0)
        continue
    if(n > k):
        if((n - k) >= k):
            print(2 * k)
        else:
            print(2 * (n - k))
        continue
    if(n < k):
        extra_count = k % n
        less_count = n - extra_count
        if(less_count < extra_count):
            print(less_count * 2) 
        elif(extra_count < less_count):
            print(extra_count * 2)
        else:
            print((extra_count * 2) - 1)
