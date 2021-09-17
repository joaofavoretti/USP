#include <iostream>
#include <cstdio>

using namespace std;

#define MAX 3


void backtracking(char *vec, int level) {
    if (level == MAX) {
        printf("%s\n", vec);
        return;
    } 

    for (char c = 'a'; c <= 'z'; c++) {
        vec[pos] = c;
        backtracking(vec, level + 1);
    }

    return;
}

int main(int argc, char *argv[]) {
    
    char p[MAX + 1];
    p[MAX] = 0;

    backtracking(p, 0);

    return 0;
}
