#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int getLength(string s,int size) {
	int score = 0;
	int count = 0;
	int first = s.find("O");
	for (int i = first; i < size; i++) {
		if (s[i] == 'O') {
			count++;
			score += count;
		}
		else {
			count = 0;
		}
	}
	return score;
}
int main() {
	int testcase;
	cin >> testcase;
	for (int i = 0; i < testcase; i++) {
		string str;
		cin >> str;
		cout << getLength(str,str.size())<<'\n';
	}
}