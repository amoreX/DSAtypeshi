#include <stdio.h>
#include <stdlib.h>

#define MAX_EDGES 100
#define MAX_VERTICES 100

// Structure to represent an edge
typedef struct
{
	char src, dest;
	int weight;
} Edge;

// Structure to represent a graph
typedef struct
{
	int V, E;
	Edge edges[MAX_EDGES];
} Graph;

// Structure for Disjoint Set (Union-Find)
typedef struct
{
	char parent[MAX_VERTICES];
	int rank[MAX_VERTICES];
} DisjointSet;

// Function to initialize the disjoint set
void makeSet(DisjointSet *ds, char vertices[], int V)
{
	for (int i = 0; i < V; i++)
	{
		ds->parent[vertices[i]] = vertices[i];
		ds->rank[vertices[i]] = 0;
	}
}

// Find operation with path compression
char find(DisjointSet *ds, char v)
{
	if (ds->parent[v] != v)
	{
		ds->parent[v] = find(ds, ds->parent[v]);
	}
	return ds->parent[v];
}

// Union operation by rank
void unionSet(DisjointSet *ds, char v1, char v2)
{
	char root1 = find(ds, v1);
	char root2 = find(ds, v2);

	if (root1 != root2)
	{
		if (ds->rank[root1] > ds->rank[root2])
		{
			ds->parent[root2] = root1;
		}
		else if (ds->rank[root1] < ds->rank[root2])
		{
			ds->parent[root1] = root2;
		}
		else
		{
			ds->parent[root2] = root1;
			ds->rank[root1]++;
		}
	}
}

// Function to compare edges by weight (used in sorting)
int compareEdges(const void *a, const void *b)
{
	return ((Edge *)a)->weight - ((Edge *)b)->weight;
}

// Kruskal's Algorithm
void kruskal(Graph *graph)
{
	DisjointSet ds;
	makeSet(&ds, (char[]){'A', 'B', 'C', 'D', 'E', 'F'}, graph->V);

	// Sort edges by weight
	qsort(graph->edges, graph->E, sizeof(Edge), compareEdges);

	printf("Minimum Spanning Tree (MST):\n");

	int edgeCount = 0;
	for (int i = 0; i < graph->E && edgeCount < graph->V - 1; i++)
	{
		Edge edge = graph->edges[i];
		if (find(&ds, edge.src) != find(&ds, edge.dest))
		{
			unionSet(&ds, edge.src, edge.dest);
			printf("(%c, %c) - %d\n", edge.src, edge.dest, edge.weight);
			edgeCount++;
		}
	}
}

// Main function
int main()
{
	Graph graph = {
		.V = 6,
		.E = 7,
		.edges = {
			{'A', 'B', 1},
			{'E', 'C', 2},
			{'C', 'F', 3},
			{'A', 'C', 4},
			{'B', 'D', 5},
			{'D', 'E', 6},
			{'E', 'F', 7}}};

	kruskal(&graph);

	return 0;
}
