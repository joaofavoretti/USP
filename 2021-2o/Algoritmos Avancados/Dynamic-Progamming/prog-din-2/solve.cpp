#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define MAX_N 1000001
#define MAX_M 10

int n, m, stones[MAX_M];
int MEMO[MAX_N];
char players[][7] = {"Stan", "Ollie"};

int solve(int t) {
    for (int j = 1; j <= t; j++) {
        MEMO[j] = 1;

        for(int i = 0; i < m; i++) {
            if (j >= stones[i] && MEMO[j - stones[i]] == 1) {
                MEMO[j] = 0;
                break;
            }
        }
    }

    return MEMO[t];
}

int main(void) {
    while(scanf("%d %d", &n, &m) == 2) {
        
        for (int i = 0; i < m; i++) {
            scanf("%d", &stones[i]);
        }

        for (int i = 0; i <= n; i++) {
            MEMO[i] = 1;
        }

        MEMO[1] = 0;
        
        cout << players[solve(n)] << " wins" << endl;
    }

}