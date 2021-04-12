def is_prime(fx):
    for i in range (2,int(fx**0.5)+1): # range(2,fx+1)로 해도 됨
        if fx%i==0:
            return 0
    return 1

if __name__=='__main__':
    x=int(input())
    print(is_prime(x))

    l1=[i for i in range(1,101) if is_prime(i)]
    print(l1)