#include <stdio.h>
#include <string.h>

void copyString(char *destination, const char *source, size_t destSize) {
    strncpy(destination, source, destSize - 1);
    destination[destSize - 1] = '\0'; // Sicherstellen, dass der Puffer nullterminiert ist
}

int main() {
    char buffer[10];
    const char *input = "This is a very long string that will cause a buffer overflow";

    printf("Source string: %s\n", input);

    copyString(buffer, input, sizeof(buffer));

    printf("Buffer content: %s\n", buffer);

    return 0;
}
