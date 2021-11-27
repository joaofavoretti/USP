#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 100

using namespace std;

int N;
int vet[MAX];

int MEMO[MAX];

int maxGlobal = 1;

int LISREC(int j) {
    if (j == 0) return 1;   // Uma cadeia com 1 elemento tem LIS == 1 !!

    int maior = 1;

    // Para todo i de de j-1 ateh 0
    for (int i = j - 1; i >= 0; i--) {
        int ret = LISREC(i);
        if (vet[i] < vet[j])
            maior = max(ret + 1, maior);
        
        // Por que nao pode? E remover esse maxGlobal
        // else
        //     maior = max(ret, maior);
    }

    if (maior > maxGlobal)
        maxGlobal = maior;
    
    return maior;
}

int LISRECPD(int j) {
    if (MEMO[j] != -1) return MEMO[j];

    int maior = 1;

    // Para todo i de de j-1 ateh 0
    for (int i = j - 1; i >= 0; i--) {
        int ret = LISRECPD(i);
        if (vet[i] < vet[j])
            maior = max(ret + 1, maior);
        // else
        //     maior = max(ret, maior);
    }

    if (maior > maxGlobal)
        maxGlobal = maior;
    
    MEMO[j] = maior;

    return MEMO[j];
}

int LISPD() {
    MEMO[0] = 1;
    
    int MEMO[j] = 1;

    for (int j = 1; j < N; j++)
    {
        for (int i = j - 1; i >= 0; i--) {
            if (vet[i] < vet[j])
                MEMO[j] = max(MEMO[i] + 1, MEMO[j]);
            // else
            //     maior = max(ret, maior);
        }
        
        if (MEMO[j] > maxGlobal)
            maxGlobal = MEMO[j];
        
        MEMO[j] = MEMO[j];
    }
    
    return MEMO[N];
}


int main(int argc, char const *argv[])
{

    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> vet[i];

    memset(MEMO, -1, sizeof(MEMO));
    MEMO[0] = 1;

    cout << "O tamanho da LIS max = " << LISPD() << endl;    

    cout << "maxGlobal = " << maxGlobal << endl;

    return 0;
}
