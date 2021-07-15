#include <bits/stdc++.h>

using namespace std;

int finder(int arr[],int start,int end,int first){
    if(start < end){
        int mid = (start + end) / 2;
        if(arr[mid] != mid + first ){
            return finder(arr,start,mid,first);
        }else{
            return finder(arr,mid + 1,end,first);
        }
    }
    return start + first;
}
int findSmallestMissedValue(int array[],int length){
    if(array[0] != 0)
        return 0;
    if(array[length - 1] == length - 1 )
        return length;
    return finder(array,0,length,array[0]);
};
int main(){
    int array[] = {0,1,2,3,7,8,9,12};
    cout<<"First Missing element is : "<<findSmallestMissedValue(array,sizeof(array) / sizeof(array[0]));
    return 0;
}