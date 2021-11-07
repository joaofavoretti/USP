#include <iostream>
#include <cstdio>
#include <climits>
#include <cstring>

#define MAX 150
#define MAX2 200

using namespace std;

int v, m, moedas[MAX];

int MEMO[MAX2];

void printVec(int *v, int tam) {
    for (int i = 0; i <= tam; i++) {
        printf("%d ", v[i]);
    }
    printf("\n");
}

int solve(int v) {
    /* nao tem mais troco. retorna 0 */
    if (v == 0) return 0;

    /* nao tem sentido trocar por moeda maior. descarta */
    if (v < 0) return INT_MAX - 1;

    int minimo = INT_MAX;

    for (int i = 0; i < m; i++) {
        minimo = min(minimo, solve(v - moedas[i]) + 1);
    }

    return minimo;
}

int solvePD(int v) {
    /* nao tem mais troco. retorna 0 */
    if (v == 0) return 0;

    /* nao tem sentido trocar por moeda maior. descarta */
    if (v < 0) return INT_MAX - 1;

    if (MEMO[v] != -1) return MEMO[v];

    int minimo = INT_MAX;
    for (int i = 0; i < m; i++) {
        minimo = min(minimo, solvePD(v - moedas[i]) + 1);
    }

    return MEMO[v] = minimo;
}

int solvePDClassico() {
    for (int j = 1; j < v + 1; ++j) {
        MEMO[j] = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (j >= moedas[i])
                MEMO[j] = min(MEMO[j], MEMO[j - moedas[i]] + 1);
        }   
    }
    
    return MEMO[v];
}

int main(int argc, char *argv[]) {

    cin >> v;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> moedas[i];
    }

    // cout << "A menor quantidade de moedas eh = " << solve(v) << endl;

    memset(MEMO, -1, sizeof(MEMO));

    // cout << "A menor quantidade de moedas eh = " << solvePD(v) << endl;
    
    MEMO[0] = 0;
    printVec(MEMO, v);
    cout << "A menor quantidade de moedas eh = " << solvePDClassico() << endl;
    printVec(MEMO, v);
    return 0;
}
