#include <iostream>
using namespace std;

class Rotate{
public:
    int *array;
    void rotate(int size){
        cout<<size << endl;
        int last = array[ size - 1];
        for (int i = size -1 ; i > 0; i--) {
            array[i] = array[i-1];
        }
        array[0] = last;
    }
    void printArray(int size){
        for (int i = 0; i < size  ; i++) {
            cout << array[i] << ' ';
        }
    }
};

int main(){
    int array[]={1,2,3,4,5};
    int size = sizeof(array) / sizeof(array[0]);
    Rotate operationArray{};
    operationArray.array = array;
    operationArray.printArray(size);
    operationArray.rotate(size);
    operationArray.printArray(size);
    return 0;
}