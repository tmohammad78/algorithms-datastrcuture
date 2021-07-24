#include <stdio.h>

void printArray(int arr[],int length){
    for(int i=0;i<length;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void swap(int *xp , int *yp){
    int temp = *xp;
    *xp = *yp ;
    *yp = temp;
}

void sortBubble(int arr[],int length){
    for(int i=0;i<length -1  ; i++){
        for (int j =0 ; j< length-i-1 ; j++){
            if (arr[j] > arr[j+1])
                swap(&arr[j], &arr[j+1]);
        }
    }
}

int main(){
    int array[] = {12,3,4,67,45,12,8,57,5};
    int length = sizeof(array) / sizeof(array[0]);
    printArray(array,length);
    sortBubble(array,length);
    printf("Sorted array: \n");
    printArray(array,length);
}

