#include <stdio.h>

int main() {
    float weight[50], profit[50], ratio[50], Totalvalue = 0.0;
    float capacity, temp;
    int n, i, j;

    printf("Enter the number of items: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("Enter Weight and Profit for item[%d]:\n", i + 1);
        scanf("%f %f", &weight[i], &profit[i]);
        ratio[i] = profit[i] / weight[i];
    }

    printf("Enter the capacity of knapsack: ");
    scanf("%f", &capacity);

    // Sorting by profit/weight ratio in descending order
    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (ratio[i] < ratio[j]) {
                temp = ratio[i]; ratio[i] = ratio[j]; ratio[j] = temp;
                temp = weight[i]; weight[i] = weight[j]; weight[j] = temp;
                temp = profit[i]; profit[i] = profit[j]; profit[j] = temp;
            }
        }
    }

    printf("\nKnapsack Problem using Greedy Algorithm (Fractional):\n");

    for (i = 0; i < n; i++) {
        if (weight[i] <= capacity) {
            Totalvalue += profit[i];
            printf("Item %d taken 100%%\n", i + 1);
            capacity -= weight[i];
        } else {
            float fraction = capacity / weight[i];
            Totalvalue += profit[i] * fraction;
            printf("Item %d taken %.2f%%\n", i + 1, fraction * 100);
            break;
        }
    }

    printf("\nMaximum value in knapsack = %.2f\n", Totalvalue);

    return 0;
}
