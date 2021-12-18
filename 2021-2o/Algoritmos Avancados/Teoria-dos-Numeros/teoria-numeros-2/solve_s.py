from collections import Counter 

def fact(n):
    i = 2
    factors = []
    while i * i <= n:
        while(n % i == 0):
            n //= i
            factors.append(i)
        i += 1
  
    if n != 1:
        factors.append(n)
  
    return Counter(factors)

while True:
    try:
        n, m = list(map(int, input().split()))

        factors = fact(m)

        max_fact = 0

        divides = True
        for prime, freq in factors.items():
            # Verifica o total de frequencia para os divisores de m
            t_freq = 0
            temp = prime
            while n >= temp:
                t_freq += n // temp
                temp = temp * prime
            if t_freq < freq:
                divides = False
                break
          
        if not divides:
            print("{} does not divide {}!".format(m, n))
        else:
            print("{} divides {}!".format(m, n))


    except(EOFError):
      break
