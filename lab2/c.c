#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>

// 1. Euclidean Algorithm for Greatest Common Divisor (GCD)
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// 2. Babylonian Algorithm for Square Root
double babylonianSqrt(double n) {
    double guess = n / 2.0;
    double epsilon = 0.00001; // Precision threshold
    while (fabs(guess * guess - n) > epsilon) {
        guess = (guess + n / guess) / 2.0;
    }
    return guess;
}

// 3. Sieve of Eratosthenes
void sieveOfEratosthenes(int n) {
    bool prime[n + 1];
    for (int i = 0; i <= n; i++)
        prime[i] = true;
    
    prime[0] = prime[1] = false;
    for (int p = 2; p * p <= n; ++p) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p)
                prime[i] = false;
        }
    }
    printf("Prime numbers up to %d: ", n);
    for (int i = 2; i <= n; ++i) {
        if (prime[i]) printf("%d ", i);
    }
    printf("\n");
}

// 4. Fibonacci Numbers
void fibonacci(int n) {
    int a = 0, b = 1, next;
    printf("Fibonacci series up to %d terms: ", n);
    for (int i = 0; i < n; ++i) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
}

// 5. Random Number Generation
void generateRandomNumbers(int count, int minVal, int maxVal) {
    srand(time(0));
    printf("Random numbers: ");
    for (int i = 0; i < count; ++i) {
        printf("%d ", minVal + rand() % (maxVal - minVal + 1));
    }
    printf("\n");
}

int main() {
    // Example executions
    printf("GCD of 56 and 98: %d\n", gcd(56, 98));
    printf("Square root of 25 using Babylonian method: %lf\n", babylonianSqrt(25));
    sieveOfEratosthenes(50);
    fibonacci(10);
    generateRandomNumbers(5, 1, 100);
    
    return 0;
}
