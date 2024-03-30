// https://leetcode.com/problems/two-sum/

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    int i, j, ival;
    int *sum = calloc(sizeof(int), 2);
    for (i = 0; i < numsSize; i++) {
        ival = nums[i];
        for (j = 0; j < numsSize; j++) {
            if (j == i) {
                j++;
            } else if ((ival + nums[j]) == target) {
                sum[0] = i;
                sum[1] = j;
                *returnSize = 2;
                return sum;
            }
        }
    }
    returnSize = 0;
    return -1;
}
