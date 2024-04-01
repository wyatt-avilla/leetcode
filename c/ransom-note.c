// https://leetcode.com/problems/ransom-note/

#include <stdbool.h>
#include <string.h>

bool canConstruct(char* ransomNote, char* magazine) {
    int notelen = strlen(ransomNote);
    int maglen = strlen(magazine);

    int noteletters[26] = {};
    int magletters[26] = {};

    int asciival;
    for (int i = 0; i < notelen; i++) {
        asciival = ransomNote[i] - 97;
        noteletters[asciival]++;
    }
    for (int i = 0; i < maglen; i++) {
        asciival = magazine[i] - 97;
        magletters[asciival]++;
    }

    for (int i = 0; i < 26; i++) {
        if (noteletters[i] > magletters[i]) {
            return false;
        }
    }
    return true;
}
