#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <climits>

using namespace std;

#define MAX_N 50
#define MAX_W 100

int N;
int W;

vector<int> P;

int MEMO[MAX_N + 1][MAX_W + 1];

void printMat(int v[][MAX_W + 1], int n, int m) {
    for (int i = n; i >= 0; i--) {
        for (int j = 0; j <= m; j++) {
            printf("%d\t", v[i][j]);
        }
        printf("\n");
    }
}

int wsspREC(int i, int peso) {
    if (i == 0) // Consumir todos os itens.. nao tem o que retornar !!
        return 0;

    if (P[i] > peso) // item nao cabe na mochila
        return wsspREC(i - 1, peso);

    return max(
        P[i] + wsspREC(i - 1, peso - P[i]), 
        wsspREC(i - 1, peso)
    );
}

int wsspRECPD(int i, int peso) {
    if (i == 0) // Consumir todos os itens.. nao tem o que retornar !!
        return 0;

    if (MEMO[i][peso] != -1) {
        return MEMO[i][peso];
    }

    if (P[i] > peso) // item nao cabe na mochila..
        MEMO[i][peso] = wsspRECPD(i - 1, peso);
    else
        MEMO[i][peso] = max(
            P[i] + wsspRECPD(i - 1, peso - P[i]), 
            wsspRECPD(i - 1, peso)
        );

    return MEMO[i][peso];
}     

int wsspPD() {
    // inicia com 0 todos os pesos do item 0
    for (int i = 0; i <= W; i++) { // condicao de fronteira
        MEMO[0][i] = 0;
    }

    for (int i = 1; i <= N; i++) // Para todos os ITENS[1..N]
        for (int j = 0; j <= W; j++) // Para todos os PESOS[0..W]
            if (P[i] > j) // item nao cabe na mochila..
                MEMO[i][j] = MEMO[i - 1][j];
            else
                MEMO[i][j] = max(P[i] + MEMO[i - 1][j - P[i]], MEMO[i - 1][j]);

    return MEMO[N][W];
} 

int main() {

    cin >> W;
    cin >> N;

    P.assign(N + 1, 0);
    
    for (int i = 0; i <= N; i++)
        cin >> P[i];

    // cout << "O peso maximo dos intervalos validos eh = " << wsspREC(N, W) << endl;

    memset(MEMO, -1, sizeof(MEMO));
    cout << "O peso maximo dos intervalos validos eh = " << wsspRECPD(N, W) << endl;
    printMat(MEMO, N, W);

    // cout << "O peso maximo dos intervalos validos eh = " << wsspPD() << endl;
    // printMat(MEMO, N, W);

    return 0;
}