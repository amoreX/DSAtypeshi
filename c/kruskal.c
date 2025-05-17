#include<stdio.h>

#define MAX 100

int parent[MAX];



int find(int i){
    while(parent[i]!=i){
        i=parent[i];
    }
    return i;
}

void unionfind(int u , int v){
    int a=find(u);
    int b =find(v);
    parent[a]=b;
}

void kruskal(int v, int e, int edges[][3]){

    int mincost=0;

    for(int i =0;i<v;i++){
        parent[i]=i;
    }

    for(int i =0;i<e;i++){
        int u =edges[i][0];
        int v =edges[i][1];
        int cost=edges[i][2];
        if(find(u)!=find(v)){
            mincost+=cost;
            printf("%d -->%d\n",u,v);
            unionfind(u,v);
        }
    }
}



int main(){
    int v,e,edges[MAX][3];

    printf("Enter total number of vertices and edges\n");
    scanf("%d",&v);
    scanf("%d",&e);
    printf("Enter source and desti and cost\n");
    for(int i=0;i<e;i++){
        scanf("%d",&edges[i][0]);
        scanf("%d",&edges[i][1]);
        scanf("%d",&edges[i][2]);
        printf("\nnext\n");
    }

    for(int i =0;i<e;i++){
        for(int j =0;j<e-1;j++){
            if(edges[j][2]>edges[j+1][2]){
                for(int k =0;k<3;k++){
                    int temp=edges[j][k];
                    edges[j][k]=edges[j+1][k];
                    edges[j+1][k]=temp;
                }
            }
        }
    }

    kruskal(v,e,edges);

}