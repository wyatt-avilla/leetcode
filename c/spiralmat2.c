#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

/**
 * return an array of arrays of size *returnSize
 * the sizes of the arrays are returned as *returnColumSizes array
 * note: both returned array and *columnSizes array must be allocated
*/
int **generateMatrix(int n, int* returnSize, int** returnColumnSizes) {
    
    *returnSize = n;
    *returnColumnSizes = (int*)calloc(n, sizeof(int));

    int** mat = (int**)calloc(n, sizeof(int*));
    for (int i = 0; i < n; i++) {
        mat[i] = (int*)calloc(n, sizeof(int));
        (*returnColumnSizes)[i] = n;
    }

    enum directions { Right, Down, Left, Up };
    int currentDirection = Right;
    int rotationCount = 0;
    int rowI = 0;
    int colJ = 0;
    int elemValue = 1;

    while (rotationCount < 4) {
        currentDirection %= 4;
        if (rowI < 0) {             // collided w/ top border
            currentDirection++;
            rotationCount++;
            rowI++;
            colJ--;
            continue;
        } else if (colJ < 0) {      // collided w/ left border
            currentDirection++;
            rotationCount++;
            colJ++;
            rowI--;
            continue;
        } else if (rowI >= n) {     // collided w/ bottom border
            currentDirection++;
            rotationCount++;
            rowI--;
            colJ--;
            continue;
        } else if (colJ >= n) {     // collided w/ right border
            currentDirection++;
            rotationCount++;
            colJ--;
            rowI++;
            continue;
        } else if (mat[rowI][colJ] != 0) {  // avoid retracing
            if (currentDirection == Right) {
                colJ--;
                rowI++;
            } else if (currentDirection == Down) {
                rowI--;
                colJ--;
            } else if (currentDirection == Left) {
                colJ++;
                rowI--;
            } else if (currentDirection == Up) {
                rowI++;
                colJ++;
            }
            currentDirection++;
            rotationCount++;
            continue;
        }

        rotationCount = 0;
        if (currentDirection == Right) {
            mat[rowI][colJ++] = elemValue++;
        } else if (currentDirection == Down) {
            mat[rowI++][colJ] = elemValue++;
        } else if (currentDirection == Left) {
            mat[rowI][colJ--] = elemValue++;
        } else if (currentDirection == Up) {
            mat[rowI--][colJ] = elemValue++;
        }
    }
    return mat;
}


int main() {

    int n = 5;
    int cols = n;
    int *rows;

    int **matrix = generateMatrix(n, &cols, &rows);

    for (int i = 0; i < n; i++) {
        printf("[");
        for (int j = 0; j < n; j++) {
            printf("%3d", matrix[i][j]);
        }
        printf(" ]\n");
    }
    printf("%d %d %d\n", n, cols, *rows );
    
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
    free(rows);


}