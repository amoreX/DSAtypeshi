#include<stdio.h>

int n;
int max(int a,int b){
    return (a> b)? a:b;
}
void knapsack(){
    int profit[n];
    int weights[n];
    int dp[100][100];
    for(int i =0;i<n;i++){
        printf("Enter the profit and the weight:\n");
        scanf("%d",&profit[i]);
        scanf("%d",&weights[i]);
    }

    int max_weight;
    printf("Enter the max weight:\n");
    scanf("%d",&max_weight);
    for(int i =0;i<=n;i++){
        for(int w=0;w<=max_weight;w++){
            if(i==0 || w==0){
                dp[i][w]=0;
            }
            else if(weights[i-1]<=w){
                dp[i][w]=max(profit[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w]);
            }
            else{
                dp[i][w]=dp[i-1][w];
            }
        }
    }

    printf("Max weight:%d\n",dp[n][max_weight]);
    int w=max_weight;
    for(int i =n;i>0 && w>0;i--){
        if(dp[i-1][w]!=dp[i][w]){
            printf("sl %d , profit %d, weight %d\n",i,profit[i-1],weights[i-1]);
            w-=weights[i-1];
        }
    }
}
int main(){
    printf("Enter number of items:\n");
    scanf("%d",&n);
    knapsack();
}
