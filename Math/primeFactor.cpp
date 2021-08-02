#include <bits/stdc++.h>
#include "iostream"

using namespace std;
bool isPrime(long int n)
{
    if (n <= 1)
        return false;
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return false;

    return true;
}
void checkNum(queue<long int>& arr,queue<long int>& prime){
    while (!arr.empty()){
        int num = arr.front();
       if(isPrime(num))
           prime.push(num);
        arr.pop();
    }
}
void showQueue(queue<long int>& q){
    while (!q.empty()){
        int num = q.front();
        cout << num << " ";
        q.pop();
    }
}
void divisor(long int number,queue<long int>& arr){
    for(int i=1 ; i<= number ; i++)
        if(number % i == 0)
            arr.push(i);
}
int main(){
    queue<long int> arr;
    queue<long int> prime;
    divisor(600851475143,arr);
    checkNum(arr,prime);
    showQueue(prime);
    return 0;
}