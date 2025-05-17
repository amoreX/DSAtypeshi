#include <stdio.h>

#define V 4

void printSolution(int reach[V][V]);

void warshall(int graph[V][V]) {
    int reach[V][V];

    // Step 1: Initialize reach matrix
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            reach[i][j] = graph[i][j];

    // Step 2: Update for transitive closure
    for (int k = 0; k < V; k++)
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                reach[i][j] = reach[i][j] || (reach[i][k] && reach[k][j]);

    // Step 3: Print result
    printSolution(reach);
}

void printSolution(int reach[V][V]) {
    printf("Transitive Closure Matrix (Reachability):\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            printf("%4d", reach[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int graph[V][V] = {
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {1, 0, 0, 0},
        {0, 0, 0, 1}
    };

    warshall(graph);
    return 0;
}
