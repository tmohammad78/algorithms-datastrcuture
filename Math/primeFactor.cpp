#include <bits/stdc++.h>
#include "iostream"
#include <list>
using namespace std;

bool isPrime(int number){
    for (int i = 2; i <= sqrt(number); i++)
        if (number % i == 0)
            return false;
    return true;
}

int divisor(int* number){
    int* arr = new int[100];
    for(int i=1 ; i<=number ; i++)
        if(number%i == 0)
            arr[i] = number;
    return arr;
}
int main(){
    int* arr = divisor(12);
    for(int i=0 ; i< 1000 ; i++)
        cout << arr[i] << " ";
    return 0;
}