"""
Algorithm to solve the Stable-Marriage problem
Entries:
    <Number of test cases>
    <N man and women inside each test case>
    <2N lines listing 
        first N woman preference list
        then N man preference list
    >
"""

from collections import deque

n_test_cases = int(input())    # Get entry of amount of test cases

# Loop through all the test_cases
for it in range(n_test_cases):
    
    N = int(input())
    
    # Creating preference lists for woman/man
    woman = [[] for _ in range(N)]
    man = [[] for _ in range(N)]

    # Read entries
    for w in range(N):
        # Entry: 1 (woman index), "list of all the N preferences"
        woman_index, preferences = input().split(' ', maxsplit = 1)
        
        woman_index = int(woman_index) - 1

        # Passar todas as 
        woman[woman_index] = list(map(lambda x: int(x) - 1, preferences.split(' ')))
    
    for m in range(N):
        # Entry: 1 (woman index), "list of all the N preferences"
        man_index, preferences = input().split(' ', maxsplit = 1)
        
        man_index = int(man_index) - 1

        man[man_index] = list(map(lambda x: int (x) - 1, preferences.split(' ')))

    
    # Algorithm of Stable Marriage
    man_available = deque([i for i in range(N)])
    woman_married = [-1 for _ in range(N)]

    while man_available:
        m = man_available.popleft()
        
        married = False

        for w in man[m]:
            if (woman_married[w] == -1):
                woman_married[w] = m 
                married = True
            else:
                for preference_man in woman[w]:
                    if preference_man == woman_married[w]:
                        break
                    elif preference_man == m:
                        man_available.append(woman_married[w])
                        woman_married[w] = m
                        married = True
                        break

            if married:
                break

    marriages = [(m, w) for (w, m) in enumerate(woman_married)]
    marriages = sorted(marriages, key=lambda x: x[0])
    
    for m, w in marriages:
        print(m + 1, w + 1)
