#include <bits/stdc++.h>
#include "iostream"

using namespace std;
bool isPrime(long long int n){
    if (n <= 1)
        return false;
    for (long long int i = 2; i < sqrt(n); i++)
        if (n % i == 0)
            return false;
    return true;
}
void showQueue(queue<long long int>& q){
    while (!q.empty()){
        int num = q.front();
        cout << num << " ";
        q.pop();
    }
}
void divisor(long long int number,queue<long long int>& arr){
    for(long long int i=1 ; i<= number ; i++){
        if(number % i == 0) {
            if(isPrime(i))
                arr.push(i);
        }
    }


}
int main(){
    queue<long long int> arr;
    divisor(600851475143,arr);
    showQueue(arr);
    return 0;
}