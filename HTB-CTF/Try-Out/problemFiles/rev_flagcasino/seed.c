#include <stdlib.h>
#include <stdio.h>

int main() {

    for(char c = 'a'; c <= 'z'; c++) {
        srand((unsigned char)c);
        int x = rand();

        printf("%c -> %d\n", c, x);
    }

    return 0;
}