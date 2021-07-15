#include <bits/stdc++.h>
using namespace std;


void findSmallestAndSecondSmallest(int array[],int length){

    int first , second = INT_MAX;
    for(int i=0 ; i<length ; i++){
        if(array[i] < first){
            second = first;
            first = array[i];
        }else if (array[i] < second && array[i] != first)
            second = array[i];
    }

    if(second == INT_MAX){
        cout << "Invalid" << ' ';
    }else {
        cout << "The smallest element is " << first << " and second "
                                                       "Smallest element is " << second << endl;
    }
}
int main(){
 int array[] = {13,34,77,2,67,45,65,3,6,9};
 int length = sizeof(array) / sizeof(array[0]);
 findSmallestAndSecondSmallest(array,length);
 return 0;
}