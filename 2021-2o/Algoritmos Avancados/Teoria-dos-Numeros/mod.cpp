#include<iostream>
#include <cstdio>

using namespace std;

// O(y)
long pot(long x, long y) {
    if (y == 0) {
        return 1;
    }

    return x * pot(x, y -1);
}

long pot_it(long x, long y) {
    long res = 1;

    while (y > 0) {
        res *= x;
        y--;
    }

    return res;
}

// versao em O(log y)
long pot_2(long x, long y) {
    if (y == 0) return 1;

    if (y % 2 == 0)
        return pot_2(x * x, y / 2);

    return x * pot_2(x * x, (y - 1) / 2);
}

long pot_2it(long x, long y) {
    long res = 1;
    while (y > 0) {
        if (y % 2 == 1) {
            res *= x;
        }
        x *= x;
        y /= 2;
    }
    return res;
}

long pot_mod(long x, long y, long p) {
    if (y == 0) return 1;

    if (y % 2 == 0)
        return pot_mod((x * x) % p, y / 2, p) % p;

    return (x * pot_mod((x * x) % p, (y - 1) / 2, p)) % p;
}

long pot_modit(long x, long y, long p) {
    long res = 1;
    while (y > 0) {
        if (y % 2 == 1) {
            res = (res * x) % p;
        }
        x = (x * x) % p;
        y = y / 2;
    }
    return res;
}

int main(int argc, char const *argv[]) {
    long x = 2;
    long y = 1e9;
    long p = 1e9 + 7;

    printf("%ld\n", pot_mod(x, y, p));

    return 0;
}
