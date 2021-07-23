#include<bits/stdc++.h>
using namespace std;
class Hash {
    int bucket ;
    list<int> *table;
public:
    Hash(int v);

    void insertItem(int x);
    void deleteItem(int x);
    int hashFunction(int x){
        return (x % BUCKET);
    };
    void displayHash();
};

void Hash::insertItem(int key) {
    int index = hashFunction(key);
    table[index].push_back(key)
}

void Hash::insertItem(int x) {
    int index = hashFunction(key);
    table[index].push_back(key);
}

Hash::Hash(int v) {
    this->bucket = v;
    table = new list<int>[bucket];
}

void Hash::deleteItem(int key) {
    int index = hashFunction(key);
    list <int> ::iterator i;
    for (i = table[index].begin(); i != table[index].end(); i++) {
        if (*i == key)
            break;
    }
    if (i != table[index].end())
        table[index].erase(i);
}
int main(){
    int a[] = {15,11,27,8,12};
    int length = sizeof(a)/sizeof(a[0]);

    Hash h(7);
}