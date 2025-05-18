#include<stdio.h>
#include<stdbool.h>
#define MAX 100
int board[MAX];

bool isSafe(int row, int col){
    for(int i =0;i<row;i++){
        if(board[i]==col || board[i] + i == col+row || board[i]-i == col-row) return false;
    }
    return true;
}


void printSoln(int n){
    for(int i =0;i<n;i++){
        for(int j=0;j<n;j++){
            if(board[i]==j){
                printf("Q");
            }
            else{
                printf("~");
            }
        }
        printf("\n");
    }
    printf("\n");
}

void solve(int n, int row){
    if (n==row){
        printSoln(n);
        return;
    }

    for(int i =0;i<n;i++){
        if(isSafe( row,  i)){
            board[row]=i;
            solve( n,  row+1);
        }
    }
}


int main(){
    printf("Enter number of rows\n");
    int n;
    scanf("%d",&n);
    solve( n,  0);
}
