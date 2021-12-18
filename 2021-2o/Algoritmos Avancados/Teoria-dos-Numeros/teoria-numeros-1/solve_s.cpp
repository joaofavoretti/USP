#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string decompFactors(int N) {
    string result;
    int factor;

    while (N != 1) {
        for (factor = 9; factor > 1; --factor) {
            if (N % factor == 0) {
                N /= factor;
                result = (char)(factor + '0') + result;
                break;
            }
        }

        if (factor == 1)
            return "-1";
    }

    return result;
}

int main(void) {
    int T, N;

    cin >> T;

    for (int t = 0; t < T; ++t) {
        cin >> N;

        if (N < 10) {
            cout << N << endl;
            continue;
        }

        cout << decompFactors(N) << endl;
    }

    return 0;
}
