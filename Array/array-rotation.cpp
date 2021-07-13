#include <bits/stdc++.h>

using namespace std;

class Operation {
    public:
    int *array;
    int arrayLength;
    int numberShift;

    void shiftItem() const{
        int temp = array[0] , i;
        for(i=0; i<arrayLength-1;i++)
            array[i] = array[i+1];
        array[arrayLength-1] = temp ;
    }

    void leftRotate() const{
        for(int i=0 ; i<numberShift ; i++){
            shiftItem();
        }
    }

    void printArr() const{
        for(int i=0;i<arrayLength ; i++)
            cout << array[i] << "";
    }
};



int main(){
    Operation myArray{};
    int arr[8] = {1,2,3,4,5,6,7,8};
    myArray.array = arr ;
    myArray.arrayLength = sizeof(arr)/sizeof(arr[0]);
    myArray.numberShift = 4;
    myArray.leftRotate();
    myArray.printArr();
}