


int ff (grafo, s, t) {
    rgraph = graph;

    maxflow = 0

    enquanto(BFS(s, t)) {
        gargalo = CalcGargalo();

        // atualiza o rgraph
        para todos os vertices da trilha {
            u, v <- trilha
            
            rgraph[u[v] -= gargalo

            rgraph[v[u] += gargalo
        } 

    }

}


int main(int argc, char const *argv[])
{
    
    printf("O fluxo maximo eh %d\n", ff(grafo, s, t));
    return 0;
}
