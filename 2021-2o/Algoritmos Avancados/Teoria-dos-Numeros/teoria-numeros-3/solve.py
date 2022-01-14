
# Calcular x^y % p
def pot_mod(x, y, p):
    res = 1
    x = x % p
    if x == 0: return 0
    
    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        x = (x * x) % p
        y = y >> 1

    return res

def sum_mod(x, y, p):
    return (x + y) % p

large_prime = 131071
while True:
    try:
        num_binary = input()[:-2]
        num_dec = 0
        len_num = len(num_binary)

        for i in range(len(num_binary)):
            num_dec = sum_mod(num_dec, int(num_binary[i]) * pot_mod(2, len_num - i - 1, large_prime), large_prime)
        
        if num_dec % large_prime == 0: print('YES')
        else: print('NO')

    except (EOFError): break
