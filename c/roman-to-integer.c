// https://leetcode.com/problems/roman-to-integer/

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

int romanToInt(char *s) {
    int convertedNum = 0;
    int stringLen = strlen(s);
    int numeralVals[] = {         // ascii value of numerals minus 65 is their index
        0, 0, 100, 500, 0, 0, 0, 0, 
        1, 0, 0, 50, 1000, 0, 0, 0, 
        0, 0, 0, 0, 0, 5, 0, 10
    };


    char currentNumeral, nextNumeral;
    int currentNumeralValue; 
    for (int i = 0; i < stringLen; i++) {
        currentNumeral = s[i];
        nextNumeral = s[i+1];
        currentNumeralValue = numeralVals[(currentNumeral - 65)];

        if (nextNumeral == '\0') {
            convertedNum += currentNumeralValue;
            break;
        } else if ((currentNumeral == 'I') && ((nextNumeral == 'V') || (nextNumeral == 'X'))) {
            currentNumeralValue *= -1;
            convertedNum += currentNumeralValue;
        } else if ((currentNumeral == 'X') && ((nextNumeral == 'L') || (nextNumeral == 'C'))) {
            currentNumeralValue *= -1;
            convertedNum += currentNumeralValue;
        } else if ((currentNumeral == 'C') && ((nextNumeral == 'D') || (nextNumeral == 'M'))) {
            currentNumeralValue *= -1;
            convertedNum += currentNumeralValue;
        } else {
            convertedNum += currentNumeralValue;
        }
    }

    return convertedNum; 
}

int main() {
    char x[] = "MCMXCIV";

    printf("%d\n", romanToInt(x));
    
}
