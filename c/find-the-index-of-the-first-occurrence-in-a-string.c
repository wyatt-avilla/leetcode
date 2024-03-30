// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

int strStr(char * haystack, char * needle) {
    int index, i = 0;
    int needleLength = strlen(needle);
    bool found = false;
    for (char currentChar = haystack[0]; (currentChar != '\0'); currentChar = haystack[++i]) {
        if (currentChar == needle[0]) {
            int k = index = i;
            for (int j = 0; j < needleLength; ) {
                found = true;
                if (needle[j++] != haystack[k++]) {
                    found = false;
                    break; 
                }
            }
            if (found) {
                break;
            }
        }
    }
    return found ? index : -1;
}

int main() {

    char *x = "sadbutsad";
    char *y = "sad";

    printf("index is %d\n", strStr(x, y));
}
