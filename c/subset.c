#include <stdbool.h>
#include <stdio.h>


bool subsetSum(int set[],int n, int d,int subset[],int* ss){
    if(d==0) return true;
    if(d<0 || n==0) return false;
    if(subsetSum(set,  n-1,  d, subset,  ss)) return true;

    subset[*ss]= set[n-1];
    (*ss)++;
    if(subsetSum(set,  n-1,  d-set[n-1], subset, ss)) return true;

    (*ss)--;
    return false;
}



int main(){
    int n;
    printf("Enter number of elements:\n");
    scanf("%d",&n);
    int set[n];
    printf("Enter:\n");
    for(int i =0;i<n;i++){
        scanf("%d",&set[i]);
    }
    int target=0;
    printf("Enter target:\n");
    scanf("%d",&target);

    int subset[100];
    int ss=0;
    if(subsetSum(set,  n,  target, subset, &ss)){
        for(int i =0;i<ss;i++){
            printf("%d , ",subset[i]);
        }
    }

}
