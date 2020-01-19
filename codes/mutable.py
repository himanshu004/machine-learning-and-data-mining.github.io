
def palindrome(str):
    if(len(str) == 1):
        return 1    
    i = 0
    j = len(str)-1
    while(i <= j):
        if(str[i] == str[j]):
            flag = 1
            i+=1
            j-=1
        else:
            flag = 0
            break;
    return flag

def main():
    s = input('Enter the string:')
    out = palindrome(s)
    if(out == 1):
        print('yes')
    else:
        print('no')
main()
