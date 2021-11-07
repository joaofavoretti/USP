#include <iostream>
#include <cstdio>
#include <vector>
#include <climits>

using namespace std;

int N;
vector<int> V;
vector<int> P;
vector<int> MEMO;

void printVet(vector<int> v, int size) {
    for (int i = 0; i < size; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}

// O(exp(n))
int wispREC(int j) {
    if (j <= 0) return P[0];

    return max(V[j] + wispREC(P[j]), wispREC(j - 1));

}

// O(n)
int wispRECPD(int j) {
    if (j <= 0) return P[0];

    if (MEMO [j] != -1) return MEMO[j];

    MEMO[j] = max(V[j] + wispRECPD(P[j]), wispRECPD(j - 1));

    return MEMO[j];
}

// O(n)
int wispPD(int j) {
    
    for (int i = 0; i <= N; i++)
    {
        MEMO[i] = max(V[i] + MEMO[P[i]], MEMO[i - 1]);
    }

    return MEMO[j];
}

int main() {

    cin >> N;

    V.assign(N + 1, 0);
    P.assign(N + 1, 0);

    for (int i = 0; i <= N; i++)
        cin >> V[i];
    
    for (int i = 0; i <= N; i++)
        cin >> P[i];

    cout << "O peso maximo dos intervalos validos eh = " << wispREC(N) << endl;

    MEMO.assign(N + 1, -1);

    printVet(MEMO, N);
    cout << "O peso maximo dos intervalos validos eh = " << wispRECPD(N) << endl;
    printVet(MEMO, N + 1);

    MEMO[0] = 0;
    cout << "O peso maximo dos intervalos validos eh = " << wispPD(N) << endl;

    return 0;
}