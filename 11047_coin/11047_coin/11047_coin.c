#define _CRT_SECURE_NO_WARNINGS
#define TRUE 1
#define FALSE 0
#include<stdio.h>
#include<stdlib.h>
int N, K;
void printCoinValue(int coin_value[]) {
	int i;
	for (i = 0; i < N; i++) {
		printf("%5d ", coin_value[i]);
	}
	printf("\n");
}
int isValidInput(int coin_value[]) {
	int i;
	if (coin_value[0] != 1)
		return FALSE;
	for (i = 1; i < N; i++) {
		if (coin_value[i] % coin_value[i - 1] != 0)
			return FALSE;
	}
	return TRUE;
}
int minCoin(int coin_value[]) {
	int recharge=K,i, result = 0;
	for (i = N - 1; i >= 0; i--) {
		if (recharge >= coin_value[i]) {
			result = result + (recharge / coin_value[i]);
			recharge = recharge % coin_value[i];
		}
	}
	return result;
}
int main() {
	int i;
	int coin_value[10];
	scanf("%d%d", &N, &K);
	if ((N > 10 || N < 1) || (K > 100000000 || K < 1)) {
		printf("bound error\n");
		exit(EXIT_FAILURE);
	}
	
	for (i = 0; i < N; i++) {
		scanf("%d", &coin_value[i]);
	}
	if (!isValidInput(coin_value)) {
		printf("bound error\n");
		exit(EXIT_FAILURE);
	}
	printf("%d\n", minCoin(coin_value));
	return 0;
}