

def lis():
    dp[0] = 1

    for j in range(1, n):
        
        dp[j] = 1

        for i in range(j - 1, -1, -1):
            if a[i] < a[j]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)


n = int(input())

dp = [-1 for i in range(n + 1)]

a = list(map(int, input().split()))

print(len(a) - lis())