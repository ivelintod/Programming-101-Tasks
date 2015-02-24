#include <iostream>
using namespace std;
int tetrahedron_filled(int *arr,int &water,int &size){
	double V;
	int br=0;
	for (int i = 0; i <size; i++)
	{
		V = (sqrt(2)*pow(*(arr+i), 3)) / 12;
		V /= 1000.0;
		if (water -V>=0&&water-V>V)
		{
			br++;
		}
	}
	return br;
}
int main()
{
	int arr1[100],number;
	cout << "Number of tethraedons= ";
	cin >> number;
	
	for (int i = 0; i < number; i++)
	{
		cout << "Enter a tethraedon's edge: ";
		cin >> arr1[i];
	}
	cout << "Water in litres = ";
	int myWater;
	cin >> myWater;
	cout <<"Number of tethraedons, filled with water are: "<< tetrahedron_filled(arr1, myWater,number) << endl;
	system("pause");
	return 0;
}