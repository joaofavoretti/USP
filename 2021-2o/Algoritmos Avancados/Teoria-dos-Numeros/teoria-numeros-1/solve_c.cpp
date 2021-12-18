
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

// Atualiza N
vi decompFactors(int N) {
    vi result;
    int factor;

    while (N != 1) {
        for (factor = 9; factor > 1; --factor) {
            if (N % factor == 0) {
                result.push_back(factor);
                N /= factor;
                break;
            }
        }

        if (factor == 1) {
            result.clear();
            result.push_back(-1);
            return result;
        }
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

        vi product_result = decompFactors(N);

        for (int i = 0; i < product_result.size(); ++i)
            cout << product_result[i];
        
        cout << endl;
    }

    return 0;
}