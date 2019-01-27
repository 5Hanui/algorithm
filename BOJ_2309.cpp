#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int arr[9], sum = 0, k = 0,j;
	cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4] >> arr[5] >> arr[6] >> arr[7] >> arr[8];
	for (int i = 0; i < 9; i++)
		sum += arr[i];
	int n = sum - 100; //1.
	sort(arr, arr + 9);//2.
	bool exit = false;
	for (k ; k < 9; k++) {
		for (j = k + 1; j < 9; j++) {
			int n1 = 0;
			n1 = arr[k] + arr[j];
			if (n1 == n) { //3.
				exit = true;
				break;
			}
		}
		if (exit == true)
			break;
	}
	for (int i = 0; i < 9; i++) {
		if (i != k & i != j) {
			cout << arr[i] << endl;//4.
		}
	}
	return 0;
}