
def opt():
    MEMO = [[0 for j in range(len(second_string) + 1)] for i in range(len(first_string) + 1)]

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            if first_string[i - 1] == second_string[j - 1]:
                MEMO[i][j] = MEMO[i - 1][j - 1] + 1
            else:
                MEMO[i][j] = max(MEMO[i - 1][j], MEMO[i][j - 1])

    return MEMO[len(first_string)][len(second_string)]

while(True):
    try:
        first_string = input()
        second_string = input()

        print(opt())

    except EOFError: break
