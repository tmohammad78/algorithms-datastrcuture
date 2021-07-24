#include <bits/stdc++.h>
using namespace std;

int finder(int arr[], int first , int last,int number){
    while (first <= last){
        int middle = (last - first) /2 + first;
        if(number == arr[middle]){
            return middle;
        }
        if(arr[middle] < number){
            first = middle+1;
        }else{
            last = middle-1;
        }
    }
    return -1;
}
int main(){
    int array[]={2, 3, 4,9, 10, 40};
    int x = 10;
    int length = sizeof(array) / sizeof(array[0]);
    int index = finder(array,0 , length -1 ,x );
    cout<< "index is " << index << " ";
}