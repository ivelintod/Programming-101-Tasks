#include <iostream>
#include<string>
using namespace std;
#include<iostream>
#include<string>
using namespace std;
string caesar_encrypt(string str, int n){
	int shift = n % 26;
	int size = str.size();
	for (int i = 0; i < size; i++)
	if (islower(str[i]))
	{
		str[i] = (str[i] - 'a' + shift) % 26 + 'a';
	}
	else if (isupper(str[i]))
	{
		str[i] = (str[i] - 'A' + shift) % 26 + 'A';
	}
	return str;
}
int main(){
	string str;
	cin >> str;
	int n;
	cout << "Enter a number: ";
	cin >> n;
	cout << caesar_encrypt(str, n) << endl;
	system("pause");
	return 0;
}