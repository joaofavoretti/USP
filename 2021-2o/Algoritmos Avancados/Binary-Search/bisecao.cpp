#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

#define ERRO 0.001

double f(double x) {
    return x*x*x - x*x + 2;
}

// De modo iterativo
double bisecao(double min, double max) {

    double mid;
    
    while (max - min > ERRO) {
        mid = (max + min) / 2;

        printf("min = %f\nmax=%f\nmid=%f\n", min, mid, max);

        if(f(mid) * f(min) < 0) max = mid;
        else min = mid;

    }

    return mid;
}

// Versao recursiva
double bissecao_rec(double min, double max) {

    double mid;

    if (max - min > ERRO) {
        mid = (max + min) / 2;

        if(f(mid) * f(min) < 0) return bissecao_rec(min, mid);
        else return bissecao_rec(mid, max);
    }

    return mid;
}

int main(int argc, char const *argv[]){

    double a, b;

    cin >> a >> b;

    if (f(a) * f(b) > 0) {
        cout << "Nao existe raiz nesse interalo" << endl;
        return 0;
    }

    cout << "Raiz: " << fixed << setprecision(2) << bisecao(a, b) << endl;

    return 0;
}