#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include "UnionFind.h"

using namespace std;

#define VISITADO 1
#define NAO_VISITADO 0
#define INF 999999999

typedef pair<int, int> ii;      // par - aresta <v, peso>
typedef vector<ii> vii;         // vetor de pares
typedef vector<int> vi;         // uso corriqueiro

// Finalmente, definimos uma lista de adj assim
//  a lista de adjacencia é um vetor de vetor de pares
int A, V;
vector <pair<int, ii>> EdgeList;
vi visitado;

void kruskal() {
    sort(EdgeList.begin(), EdgeList.end()); // ordena as arestas em ordem crescente

    UnionFind uf(A);                        // cria uma união de conjuntos de tamanho A (nós)

    int custoMin = 0;

    for (int i = 0; i < EdgeList.size(); i++)
    {
        pair<int, ii> par = EdgeList[i];
        ii aresta = par.second;
        int u = aresta.first;
        int v = aresta.second;
        int w = par.first;

        // se u e v sao arvores distintas.. computa o MST e junta as arvores
        if (!uf.isSameSet(u, v)) {
            custoMin = custoMin + w;        // acumula o custo
            uf.unionSet(u, v);
        }
    }

    printf("O custo minimo da MST eh: %d\n", custoMin);
}

int main(int argc, char const *argv[])
{
    int u, v, w;

    cin >> A;
    cin >> V;

    for (int i = 0; i < A; i++) {
        cin >> u >> v >> w;
        EdgeList.push_back(make_pair(w, ii(u, v)));
    }


    for (int i = 0; i < V; i++) {
        visitado.push_back(NAO_VISITADO);
    }
    
    kruskal();

    return 0;
}