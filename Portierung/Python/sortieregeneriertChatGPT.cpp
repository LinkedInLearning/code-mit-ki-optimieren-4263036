#include <stdio.h>

void sort_numbers(int numbers[], int length) {
    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) {
            if (numbers[i] > numbers[j]) {
                int temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
}

int main() {
    int numbers[] = {5, 2, 9, 1, 5, 6};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    sort_numbers(numbers, length);

    printf("Sorted numbers: ");
    for (int i = 0; i < length; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
