#include <bits/stdc++.h>
using namespace std;

void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}
void insertionSort(int arr[],int length){
    int i , j , key ;
    for(i = 1 ;i<length ; i++){
        key = arr[i];
        j= i-1;
        while(j>=0 && arr[j] > key){
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = key;
    }
}

int main(){
    int arr[]= { 2,12,5,7,9,10};
    int length = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, length);
    printArray(arr, length);
    return 0;
}

