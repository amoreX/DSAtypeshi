#include<stdio.h>
#include<stdlib.h>

#define MAX 100

void prim(int adj[MAX][MAX],int n){
	int edgecount=0;
	int mincost=0;
	int visited[MAX]={0};

	visited[0]=1;

	while (edgecount<n-1){
		int min=999;
		int a=-1;
		int b=-1;
		for(int i =0;i<n;i++){
			if(visited[i]){
				for(int j=0;j<n;j++){
					if(!visited[j] && adj[i][j]<min){
						min=adj[i][j];
						a=i;
						b=j;
					}
				}
			}
		}

		if(a!= -1 && b!=-1){
			edgecount++;
			mincost+=min;
			//print
			visited[b]=1;
		}
	}
}
int main(){
	int n,adj[MAX][MAX];
	//get adj matrtix done if ==0 then 999

	prim(adj,n);
}
