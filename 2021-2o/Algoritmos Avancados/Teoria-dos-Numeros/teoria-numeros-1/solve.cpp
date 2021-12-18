#include <iostream>
#include <cstdio>
#include <bitset>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;
typedef map<ll, int> mli;

#define MAX 10000000
#define MAX_BITSET 10000010

ll tam_crivo;
bitset<MAX_BITSET> crivo;  // 10⁹ cobre a maioria dos casos
                        // 8 vezes mais economico
vector<ll> fatoresPrimos;


void criaCrivo(ll tamanho) {
    tam_crivo = tamanho + 1;

    // seta todos os valores para 1
    crivo.set();

    // 0 e 1 nao sao primos
    crivo[0] = crivo[1] = 0;

    for (ll i = 2; i < tam_crivo; i++ ) {
        // Para cada número PRIMO já descoberto, elimina seus múltiplos
        if (crivo[i]) {
            // Armazena o numero primo
            fatoresPrimos.push_back(i);

            // j = 2 ou j = i * i (??)
            for (ll j = 2 * i; j < tam_crivo; j += i) {
                crivo[j] = 0;
            }
        }
    }
}

// Verificacao usando crivo e fatores primos
bool ehPrimo(ll numero) {
    if (numero < tam_crivo) {
        return true;
    }

    for (ll i = 0; i < fatoresPrimos.size() && fatoresPrimos[i] * fatoresPrimos[i] < numero; i++) {
        if (numero % fatoresPrimos[i]) {
            return true;
        }
    }

    return false;
}

// Uma funcao que retorna os fatores primos de um numero
vll primeFactors(ll N) {
    // comeca pelo 2
    ll ind = 0;
    ll PF = fatoresPrimos[ind];
    vll fatores;

    // Basta ir até a raiz quadrada
    while(PF * PF <= N) {
        while(N % PF == 0) {
            fatores.push_back(PF);
            N /= PF;
        }

        PF = fatoresPrimos[++ind];
    }

    // O N é primo e portanto ele é fator de si próprio
    if (N != 1) {
        fatores.push_back(N);
    }

    return fatores;
}

// Uma funcao que retorna os fatores primos de um numero
mli primeFactorsMAP(ll N) {
    // comeca pelo 2
    ll ind = 0, PF = fatoresPrimos[ind];
    mli fatores;

    // Basta ir até a raiz quadrada
    while(PF * PF <= N) {
        while(N % PF == 0) {
            // insere no mapa
            fatores[PF]++;
            N /= PF;
        }

        PF = fatoresPrimos[++ind];
    }

    // O N é primo e portanto ele é fator de si próprio
    if (N != 1) {
        fatores[N]++;
    }
    
    return fatores;
}

int main(int argc, char const *argv[])
{
    // Cria o crivo de 10⁷
    criaCrivo(MAX);

    int n_testes;
    cin >> n_testes;

    for (int i = 0; i < n_testes; i++) {
        ll N;
        bool a = false;
        cin >> N;

        if (N == 1) {
            cout << "1" << endl;
            continue;
        }

        vll fatores = primeFactors(N);

        vll novos_fatores;
        for (int j = 0; j < fatores.size(); j++) {
            if (fatores[j] > 10) {
                a = true;
                break;
            }

            if (j < fatores.size() - 2) {
                if (fatores[j] * fatores[j + 1] * fatores[j + 2] < 10) {
                    novos_fatores.push_back(fatores[j] * fatores[j + 1] * fatores[j + 2]);
                    j += 2;
                    continue;
                }
            }

            if (j < fatores.size() - 1) {
                if (fatores[j] * fatores[j + 1] < 10) {
                    novos_fatores.push_back(fatores[j] * fatores[j + 1]);
                    j++;
                    continue;
                }
            }

            novos_fatores.push_back(fatores[j]);
        }

        if (a) {
            cout << -1 << endl;
        } else {
            for (int j = 0; j < novos_fatores.size(); j++) {
                cout << novos_fatores[j] << "";
            }
            cout << endl;
        }
    }

    return 0;
}

