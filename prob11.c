#include <stdio.h>

int lineProduct(int currentI, int currentJ, int grid[][20]) {
    if(currentJ + 3 < 20) {
        int j;
        int lp = 1;
        for(j = currentJ; j < currentJ + 4; j++)
            lp *= grid[currentI][j];
        return lp;
    } else {
        return 0;
    }
}


int columnProduct(int currentI, int currentJ, int grid[][20]) {
    if(currentI + 3 < 20) {
        int i;
        int cp = 1;
        for(i = currentI; i < currentI + 4; i++)
            cp *= grid[i][currentJ];
        return cp;
    } else {
        return 0;
    }
}


int diagonalProduct(int currentI, int currentJ, int grid[][20]) {
    if(currentI + 3 < 20 && currentJ + 3 < 20) {
        int sum;
        int dp = 1;
        for(sum = 0; sum < 4; sum++)
            dp *= grid[currentI + sum][currentJ + sum];
        return dp;
    } else {
        return 0;
    }
}

int otherDiagonalProduct(int currentI, int currentJ, int grid[][20]) {
    if(currentI + 3 < 20 && currentJ - 3 >= 0) {
        int sum;
        int dp = 1;
        for(sum = 0; sum < 4; sum++)
            dp *= grid[currentI + sum][currentJ - sum];
        return dp;
    } else {
        return 0;
    }
}


int findHighestProduct(int currentI, int currentJ, int grid[][20]) {
    int lp = lineProduct(currentI, currentJ, grid);
    int cp = columnProduct(currentI, currentJ, grid);
    int dp = diagonalProduct(currentI, currentJ, grid);
    int odp = otherDiagonalProduct(currentI, currentJ, grid);
    if(dp > lp && dp > cp && dp > odp)
        return dp;
    else if(cp > lp && cp > odp)
        return cp;
    else if(lp > odp)
        return lp;
    else
        return odp;
}

int main() {
    int grid[20][20];
    int i;
    int j;
    for(i = 0; i < 20; i++)
        for(j = 0; j < 20; j++)
            scanf("%d", &grid[i][j]);

    int maxProduct = 1;
    int currentProduct;
    for(i = 0; i < 20; i++) {
        for(j = 0; j < 20; j++) {
            currentProduct = findHighestProduct(i, j, grid);
            if(currentProduct > maxProduct)
                maxProduct = currentProduct;
        }
    }

    printf("%d\n", maxProduct);

    return 0;
}
