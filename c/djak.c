#include<stdio.h>
#include <stdbool.h>
#define V 6
#define INF 999999

int minD(bool visited[],int dist[]){
    int mind_index=-1;
    int minval=INF;

    for(int v=0;v<V;v++){
        if(!visited[v] && dist[v]<minval){
            minval=dist[v];
            mind_index=v;
        }
    }
    return mind_index;
}


void djak(int graph[V][V],int source){
    bool visited[V];
    int dist[V];
    for(int i=0;i<V;i++){
        visited[i]=false;
        dist[i]=INF;
    }

     dist[source] = 0;

    for(int count=0;count<V-1;count++){
        int u=minD(visited,  dist);
        if(u==-1) break;
        visited[u]=true;

        for(int v=0;v<V;v++){
            if(!visited[v] && graph[u][v]!=0 && dist[u]+graph[u][v] <dist[v]){
                dist[v]=dist[u]+graph[u][v];
            }
        }
    }

    for(int i =0;i<V;i++){
        if(i!=source){
            if(dist[i]!=INF){
                printf("%d\t\t%d\n", i+1, dist[i]);
            }
        }
    }
}

int main(){
    int graph[V][V] = {
        {0, 2, 4, 0, 0, 0},
        {2, 0, 1, 7, 0, 0},
        {4, 1, 0, 0, 3, 0},
        {0, 7, 0, 0, 2, 1},
        {0, 0, 3, 2, 5, 0},
        {0, 0, 0, 1, 0, 0}
    };
    printf("Enter source:\n");
    int n;
    scanf("%d",&n);
    djak(graph,n);
}
