#include "iostream"

using namespace std;

int finder(int number,int arr[], int length){
    for(int i =0 ; i<length ; i++){
        if(number == arr[i])
            return i;
    }
    return -1;
}

int main(){
    int arr[] = {6,12,43,65,122,123};
    int numberToFind = 65;
    int length = sizeof(arr) / sizeof(arr[0]);
    int index = finder(numberToFind,arr,length);
    if(index == -1){
        cout<< "The index of number not found "<< " ";
    }
    cout<< "The index of number is : " << index << " ";
}