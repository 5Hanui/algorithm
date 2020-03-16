#include <iostream>
#include <vector>
using namespace std;
vector<int> num;
int N;
int loc;
int penguin() {
	int s1 = num[0], s2 = num[N-1];
	for (int i = 0; i < loc; i++) {
		if (s1 >= num[i]) s1 = num[i];
	}
	for (int i = N-1; i > loc; i--) {
		if (s2 >= num[i]) s2 = num[i];
	}
	return s1 + s2;

}
int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int n;
		cin >> n;
		if (n == -1) loc = i;
		num.push_back(n);
	}
	cout<< penguin() << endl;
}