def collatz_minus(N=1):
    minus = []
    while len(minus) != 4:
        count = 0
        n = N
        while n != 1:
            if count > 500:
                if minus.count(int(N)):
                    minus.append(int(N))

            if n % 2 == 0:
                n /= 2
                count += 1
            else:
                n = n * 3 + 1
                count += 1
        N += 1
        
        
    return minus

print(collatz_minus())
