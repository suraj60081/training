#include<iostream>

using namespace std;

int FindPos(int arr[],int n, int key)
{
	for(int i=0;i<n;i++)
	{
		if(arr[i]==key) return i+1;
	}
	return -1;
}

int main()
{
	int arr[5] = {1,2,3,4,8};
	int key;
	cin>>key;
	cout<<FindPos(arr, 5, key);
	
	return 0;
}
