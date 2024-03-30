// https://leetcode.com/problems/fizz-buzz/

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

char ** fizzBuzz(int n, int *returnSize) {
    char **retarr = calloc(sizeof(char*), n);
    char *fstr = calloc(sizeof(char), 5);
    char *bstr = calloc(sizeof(char), 5);
    char *fbstr = calloc(sizeof(char), 9);

    strncpy(fstr, "Fizz", 5);       //
    strncpy(bstr, "Buzz", 5);       // caller should free these
    strncpy(fbstr, "FizzBuzz", 9);  //

    for (int i = 0; i < n; i++) {
        if ((((i+1) % 3) == 0) && (((i+1) % 5) == 0)) {
            retarr[i] = fbstr;
        } else if (((i+1) % 3) == 0) {
            retarr[i] = fstr;
        } else if (((i+1) % 5) == 0) {
            retarr[i] = bstr;
        } else {
            int digitcount = 0;
            int icopy = (i+1);
            while (icopy != 0) {
                icopy /= 10;
                digitcount++;
            }
            char *intstr = calloc(sizeof(char), digitcount+1);
            snprintf(intstr, (digitcount+1), "%d", (i+1));
            retarr[i] = intstr;
        }
    }
    *returnSize = n;    // ???????
    return retarr;
}

int main() {

    int n = 15;
    char **x = fizzBuzz(n, &n);
    for (int i = 0; i < n; i++) {
        printf("%s\n", x[i]);
    }
    

}
