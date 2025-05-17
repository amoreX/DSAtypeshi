#include <stdio.h>

#define V 4
#define INF 99999

void printSolution(int dist[V][V]);

void floydWarshall(int graph[V][V]) {
    int dist[V][V];

    // Initialize distance matrix with the input graph
    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            dist[i][j] = graph[i][j];

    // Floyd-Warshall algorithm
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    // Print the result
    printSolution(dist);
}

void printSolution(int dist[V][V]) {
    printf("All-Pairs Shortest Path Matrix:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF)
                printf("%7s", "INF");
            else
                printf("%7d", dist[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int graph[V][V] = {
        {0,   5,   8, 9},
        {34,   0,   1, 23},
        {7, 17,   0,   9},
        {8, 11, 4,   0}
    };

    floydWarshall(graph);
    return 0;
}
