#include <bits/stdc++.h>
using namespace std;

const int ALPHABET_SIZE = 26;

struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    bool isEndOfWord;
};

struct TrieNode* getNode(void){
    struct TrieNode *pNode = new TrieNode;
    pNode->isEndOfWord = false;
    for(int i=0 ; i<ALPHABET_SIZE ;i++)
        pNode->children[i]=NULL;
    return pNode;
}

void insert(struct TrieNode *root,string key){
    struct TrieNode *newNode = root;
    for(int i=0 ;i<key.length() ; i++){
        int index = key[i] - 'a';
        if(!newNode->children[index])
            newNode->children[index]=getNode();
        newNode = newNode->children[index];

    }
    newNode->isEndOfWord = true;
}
bool search(struct TrieNode *root, string key)
{
    struct TrieNode *newNode = root;

    for (int i = 0; i < key.length(); i++)
    {
        int index = key[i] - 'a';
        if (!newNode->children[index])
            return false;

        newNode = newNode->children[index];
    }

    return (newNode->isEndOfWord);
}

int main(){
    string keys[] = {"the", "a", "there",
                     "answer", "any", "by",
                     "bye", "their" };
    int n = sizeof(keys)/sizeof(keys[0]);
    struct TrieNode* root =getNode();
    for (int i = 0; i < n; i++)
        insert(root, keys[i]);
    cout << "Exist 'The' : " << search(root, "the") << "\n";
    cout << "Exist 'These' : " << search(root, "these") << "\n";
    cout << "Exist 'answer' : " << search(root, "answer") << "\n";
    return 0;
}