#include<stdio.h>

int a[6][6] = {
        // 0 1 2 3 4 5
        {0, 0, 1, 0, 0, 0},  // 0 -> 2
        {0, 0, 1, 1, 0, 0},  // 1 -> 2,3
        {0, 0, 0, 0, 1, 0},  // 2 -> 4
        {0, 0, 0, 0, 1, 1},  // 3 -> 4,5
        {0, 0, 0, 0, 0, 1},  // 4 -> 5
        {0, 0, 0, 0, 0, 0}   // 5 -> no outgoing edges
    };

int n=6;
int indegre[6];
void in_degre(){
    for(int i=0;i<n;i++){
        int sum=0;
        for(int j=0;j<n;j++){
            sum+=a[j][i];
        }
        indegre[i]=sum;
    }
}

void topology(){
    in_degre();
    int top=-1;
    int s[n];
    for(int i =0;i<n;i++){
        if(indegre[i]==0){
            s[++top]=i;
        }
    }

    int t[n];
    int k=0;
    while(top!=-1){
        int u=s[top--];
        t[k++]=u;

        for(int v=0;v<n;v++){
            if(a[u][v]==1){
                indegre[v]--;
                if(indegre[v]==0) s[++top]=v;
            }
        }
    }

    for(int i=0;i<n;i++){
        printf("%d,",t[i]);
    }
}


int main(){
    topology();
}
