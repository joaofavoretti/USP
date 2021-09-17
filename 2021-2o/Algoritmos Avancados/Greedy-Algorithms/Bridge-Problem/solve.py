"""
Bridge-Torch problem for N >= 1
author: Joao Pedro Favoretti
"""

# Number of test cases
T = int(input())

for _ in range(T):
    input()
    N = int(input())


    # Time to cross vector
    Pers = []
    for n in range(N):
        p = int(input())
        Pers.append(p)
        
    Pers = sorted(Pers)

    time = 0
    crosses = []

    while(Pers):
        if len(Pers) > 3:
            if (Pers[0] + 2*Pers[1] + Pers[-1]) < (2*Pers[0] + Pers[-2] + Pers[-1]): 
                crosses.append((Pers[0], Pers[1]))
                time += Pers[1]

                crosses.append(tuple([Pers[0]]))
                time += Pers[0]
                
                crosses.append((Pers[-2], Pers[-1]))
                time += Pers[-1]

                crosses.append(tuple([Pers[1]]))
                time += Pers[1]
            else:
                crosses.append((Pers[0], Pers[-2]))
                time += Pers[-2]

                crosses.append(tuple([Pers[0]]))
                time += Pers[0]

                crosses.append((Pers[0], Pers[-1]))
                time += Pers[-1]

                crosses.append(tuple([Pers[0]]))
                time += Pers[0]

            Pers = Pers[:-2]
        elif len(Pers) == 3:
            crosses.append((Pers[0], Pers[1]))
            time += Pers[1]
            
            crosses.append(tuple([Pers[0]]))
            time += Pers[0]

            crosses.append((Pers[0], Pers[-1]))
            time += Pers[-1]
            
            Pers = []
        else:
            crosses.append(tuple(Pers))
            time += Pers[-1]

            Pers = []

    print(time)

    # Print crosses
    for c in crosses:
        if len(c) == 1:
            print(c[0])
        else:
            print(c[0], c[1])
    
    # Correct new line problem
    if _ < T-1:
        print()
