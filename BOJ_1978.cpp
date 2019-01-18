#include <iostream>
#include <math.h>
using namespace std;
int is_prime(int num) {
	if (num == 1) return false;
	int sqrn = (int)sqrt(num);
	int i = 2;
	while (i <= sqrn) {
		if (num%i == 0) return false; //소수가 아니면 f
		i++;
	}
}
int main() {
	int n, num, count = 0;
	cin >> n;
	for(int i=0;i<n;i++){
		cin >> num;
		if(is_prime(num))	++count;
	}
	cout << count;
	return 0;
}