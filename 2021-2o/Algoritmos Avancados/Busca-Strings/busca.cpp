#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

void busca(string texto, string patt, int tamt, int tamp) {
    // Busca no texto inteiro
    for (int i = 0; i < tamt - tamp + 1; i++) {
        bool achou = true;
        
        for (int j = 0; j < tamp & achou; j++) {
            if (texto[i + j] != patt[j]) {
                achou = false;
            }
        }

        if (achou)
            printf("Encontrei o padrao em %d\n", i);
    }
}

int main(int argc, char const *argv[]) {
    string texto;
    string patt;

    getline (cin, texto);
    getline (cin, patt);

    int tamt = texto.length();
    int tamp = patt.length();

    busca(texto, patt, tamt, tamp);

    return 0;
}
