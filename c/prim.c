#include<stdio.h>
#include<stdlib.h>
#define MAX 100


void prims(int n , int adj[MAX][MAX]){
    int visited[MAX]={0};
    int edgecount=0;
    int min=0;
    visited[0]=1;
    
    while(edgecount<n-1){
        int a=-1;
        int b=-1;
        int mincost=999;
        for(int i=0;i<n;i++){ 

            if(visited[i]){
                for(int j=0;j<n;j++){
                    if(!visited[j] && adj[i][j]<=mincost){
                        a=i;
                        b=j;
                        mincost=adj[i][j];
                    }
                }
            }
        }
        if(a!=-1 && b!=-1){
            edgecount++;
            visited[b]=1;
            min+=mincost;
            printf("%d-->%d\n",a,b);
        }
    }
}



int main(){
    int n , adj_cost[MAX][MAX];
    n=4;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&adj_cost[i][j]);
            if(adj_cost[i][j]==0){
                adj_cost[i][j]=999;
            }
        }
    }

    prims(n,adj_cost);
}