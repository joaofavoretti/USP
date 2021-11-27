#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

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
vector<vii> AdjList(100);
vi visitado;

void printAdjlist() {
    for (int i = 0; i < V; i++)
    {
        printf("%d -> ", i);
        for (int j = 0; j < AdjList[i].size(); j++)
        {
            if (j < AdjList[i].size() - 1)
                printf("(%d,%d) > ", AdjList[i][j].first, AdjList[i][j].second);
            else
                printf("(%d,%d)\n", AdjList[i][j].first, AdjList[i][j].second);
        }
        
        
    }
    
}

void dfs(int u) {
    visitado[u] = VISITADO;                         // Marca o vertice como visitado
    printf("%d ", u);
    for (int i = 0; i < AdjList[u].size(); i++) {   // Para todo v adjacente a u
        ii par = AdjList[u][i];                     // par = aresta <v, peso>
        int v = par.first;                          // v = vertice adjacente a u
        int peso = par.second;                      // peso = peso da aresta (u, v)
        
        if (visitado[v] == NAO_VISITADO) {          // Se v nao foi visitado
            dfs(v);                                 // visita v
        }
    }
}

void bfs(int u) {
    queue<int> q;                                   // Fila de vertices visitados
    vi vertice(V, INF);                        // Distancia inicial infinita

    vertice[u] = 0;                                 // Distancia do vertice inicial = 0

    q.push(u);                                      // Insere o vertice inicial na fila

    while(!q.empty()) {
        int k = q.front();                         // k = primeiro vertice da fila
        q.pop();                                   // Remove o primeiro vertice da fila

        printf(">> %d ", k);

        for (int i = 0; i < AdjList[k].size(); i++)
        {
            ii par = AdjList[k][i];                // par = aresta <v, peso>
            int v = par.first;                     // v = vertice adjacente a k
            int peso = par.second;                 // peso = peso da aresta (k, v)

            if (vertice[v] == INF) {
                vertice[v] = vertice[k] + 1;        // Atualiza a distancia do vertice v
                q.push(v);
            }
        }
        
    }

}

int main(int argc, char const *argv[])
{
    int u, v, w;

    cin >> A;
    cin >> V;

    for (int i = 0; i < A; i++) {
        cin >> u >> v >> w;
        AdjList[u].push_back(make_pair(v, w));    
        AdjList[v].push_back(make_pair(u, w));  // Caso que o grafo seja direcionado
    }

    printAdjlist();

    for (int i = 0; i < V; i++) {
        visitado.push_back(NAO_VISITADO);
    }
    
    // Percorrer o grafo em profundidade...
    // dfs(0);
    bfs(0);

    return 0;
}

