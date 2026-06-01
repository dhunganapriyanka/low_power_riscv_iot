int main() {
    int data[8] = {22, 23, 24, 23, 22, 25, 24, 23};
    int sum = 0;

    for (int i = 0; i < 8; i++) {
        sum += data[i];
    }

    int average = sum / 8;
    return average;
}
