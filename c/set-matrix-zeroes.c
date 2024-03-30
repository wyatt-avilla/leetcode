// https://leetcode.com/problems/set-matrix-zeroes/

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>


void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {

    int *zeroRows = (int*) calloc(matrixSize, sizeof(int));
    int *zeroCols = (int*) calloc(*matrixColSize, sizeof(int));

    int i, j;
    for (i = 0; i < matrixSize; i++) {
        for (j = 0; j < *matrixColSize; j++) {
            if (matrix[i][j] == 0) {
                zeroRows[i] = 1;
                zeroCols[j] = 1;
            }
        }
    }

    int targetRow;
    for (int i = 0; i < matrixSize; i++) {
        if (zeroRows[i] == 1) {
            targetRow = i;
            for (int j = 0; j < *matrixColSize; j++) {
                matrix[targetRow][j] = 0;
            }
        }
    }
    
    int targetCol;
    for (int i = 0; i < *matrixColSize; i++) {
        if (zeroCols[i] == 1) {
            targetCol = i;
            for (int j = 0; j < matrixSize; j++) {
                matrix[j][targetCol] = 0;
            }
        }
        
    }
    

    free(zeroCols);
    free(zeroRows);

}

int main() {

    int rows = 3;
    int cols = 4;

    int** mat = (int**)calloc(rows, sizeof(int*));
    for (int i = 0; i < rows; i++) {
        mat[i] = (int*)calloc(cols, sizeof(int));
        mat[i][0] = 1;
        mat[i][1] = 1;
        mat[i][2] = 1;
        mat[i][3] = 1;
    }
    mat[0][0] = 0;
    mat[0][3] = 0;

 
    for (int i = 0; i < rows; i++) {        // printer
        printf("[");
        for (int j = 0; j < cols; j++) {
            printf(" %d", mat[i][j]);
        }
        printf(" ]\n");
    }
       
    setZeroes(mat, rows, &cols);
    printf("-----------\n");

    for (int i = 0; i < rows; i++) {        // printer
        printf("[");
        for (int j = 0; j < cols; j++) {
            printf(" %d", mat[i][j]);
        }
        printf(" ]\n");
    }
    

    for (int i = 0; i < rows; i++) {
        free(mat[i]);
    }
    free(mat);
}
