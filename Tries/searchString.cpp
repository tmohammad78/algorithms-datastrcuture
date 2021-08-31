#include <bits/stdc++.h>
using namespace std;

struct Trie{
    Trie* array[27] = NULL;
    int index;
};

Trie* root = new Trie()
void insert(){

}

int search(){

}

void findMatch(string words[],int n,vector<vector<string>> Q){
    string temp,t;
    for(int i=0 ; i< n ;i++){
        temp = "{" + words[i];
        for (int j = words[i].size()-1;j>=0 ;j--){
            t = word[i][j] + temp;
            insert(t,i);
        }
    }

    for(int i =0 ; i< Q.size(); i++){
        string prefix = = Q[i][0];
        string suffix =  Q[i][1];
        string tempN = prefix+ "{"+suffix;
        int res = search(tempN);
        if(res != -1){
            cout << words[res] << " ";
        }else {
            cout << "-1\n" << " ";
        }
    }
}
int main(){
    string arr[]
            = { "apple", "app", "biscuit",
                "mouse", "orange", "bat",
                "microphone", "mine" };
    int N = 8;
    vector<vector<string>> Q = { { "a", "e" }, { "mi", "ne" } };
    findMatch(arr, N, Q);
    return 0;
}