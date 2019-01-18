#include <iostream>
using namespace std;
int gcd(int u, int v) {
	if (v == 0) return u;
	else
		return gcd(v, u%v);
}
int main() {
	int num1, num2,result_gcd,result_lcd;
	cin >> num1 >> num2;
	result_gcd = gcd(num1, num2);
	cout << result_gcd << endl;
	cout << (num1*num2) / result_gcd << endl;
	return 0;
}