#include <iostream>
#include <string>
using namespace std;
void lucky(string s) {
	int len = s.size() / 2;
	int sum1 = 0, sum2 = 0;
	for (int i = 0; i < len; i++) {
		int n1 = s[i] - '0';
		int n2 = s[i + len] - '0';
		sum1 += n1;
		sum2 += n2;
	}
	if (sum1 == sum2)
		cout << "LUCKY" << endl;
	else if(sum1!=sum2)
		cout << "READY" << endl;
}

int main() {
	string num;
	cin >> num;
	lucky(num);
}