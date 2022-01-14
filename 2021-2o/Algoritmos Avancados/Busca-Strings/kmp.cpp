#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define TAM 260010

using namespace std;

void kmpPreProcessamento(int *b, string patt) {
    int tamp = patt.length();

    int i = 0, j = -1;
    b[0] = -1;

    while(i < tamp) {
        printf("%d\n", j);
        while (j >= 0 && patt[i] != patt[j]) {
            j = b[j];
        }

        i++;
        j++;
        b[i] = j;
    }

}

int main(int argc, char const *argv[]) {
    int b[1001];
    string texto;
    string patt;

    getline (cin, texto);
    getline (cin, patt);

    int tamt = texto.length();
    int tamp = patt.length();

    kmpPreProcessamento(b, patt);

    return 0;
}
