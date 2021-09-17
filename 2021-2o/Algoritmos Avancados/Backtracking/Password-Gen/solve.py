"""
Password Generator problem
Backtracking Algorithm
author: Joao Pedro Favoretti
"""
import sys

def backtracking(rule, words, rulesIt, password):
    if rulesIt >= len(rule):
        # Print password
        for word in password:
            print(word, end='')
        print()
        return

    # Iterar pelas palavras
    if rule[rulesIt] == '#':
        for word in words:
            password.append(word)
            backtracking(rule, words, rulesIt + 1, password)
            password.pop()

    # Iterar pelas letras 0-9
    elif rule[rulesIt] == '0':
        for number in range(10):
            password.append(number)
            backtracking(rule, words, rulesIt + 1, password)
            password.pop()

# Loop principal
for n in sys.stdin:
    n = int(n)

    # Number of words
    words = []
    for word in range(n):
        w = input()
        words.append(w)

    # Number of rules
    m = int(input())
    rules = []
    for rule in range(m):
        r = input()
        rules.append(r)
    
    for rule in rules:
        print('--')
        backtracking(rule, words, 0, [])

