// You have weighted edges, you sort them , and then take the one's in increasing order jisse ki cycle na bane

#include <stdio.h>
#include <stdlib.h>

#define max_edges 100
#define max_vertices 100

typedef struct
{
	char src, dest;
	int weight;
} edge;

typedef struct
{
	int V, E;
	edge edges[max_edges];
} graph;

typedef struct
{
	char parent[max_vertices];
	int rank[max_vertices];
} disjoint;

void makeSet(disjoint *d, char vertices[], int V)
{
	for (int i = 0; i < V; i++)
	{
		d->parent[vertices[i]] = vertices[i];
		d->rank[vertices[i]] = 0;
	}
};

int compareEdges(const void *a, const void *b)
{
	return ((edge *)a)->weight - ((edge *)b)->weight;
};

char find(disjoint *d, char v)
{
	if (d->parent[v] != v)
	{
		d->parent[v] = find(d, d->parent[v]);
	}
	return d->parent[v];
}

void unionSet(disjoint *ds, char v1, char v2)
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

void kruskal(graph *g)
{

	disjoint ds;
	makeSet(&ds, (char[]){'A', 'B', 'C', 'D', 'E', 'F'}, g->V);

	qsort(g->edges, g->E, sizeof(edge), compareEdges);

	int edgecount = 0;

	for (int i = 0; i < g->E && edgecount < g->V - 1; i++)
	{
		edge edge = g->edges[i];
		if (find(&ds, edge.src) != find(&ds, edge.dest))
		{
			unionSet(&ds, edge.src, edge.dest);
			printf("(%c, %c) - %d\n", edge.src, edge.dest, edge.weight);
			edgecount++;
		}
	}
};

int main()
{
	graph graph = {
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