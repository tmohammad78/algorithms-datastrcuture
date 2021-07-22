#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data ;
    struct Node *left, *right;
};

Node* newNode(int number){
    Node* temp = new Node;
    temp->data = number;
    temp->left = temp->right = NULL;
    return temp;
}

void printNodeTraversal(Node* root){
    if(root == NULL){
        return;
    }
    queue<Node *> q;
    q.push(root);
    while(!q.empty()){
        Node* node = q.front();
        cout << node->data << " ";
        q.pop();
        if(node->left != NULL){
            q.push(node->left);
        }
        if(node->right != NULL){
            q.push(node->right);
        }
    }
}
int main(){
   Node* root = newNode(1);
   root->left = newNode(2);
   root->right = newNode(3);
   root->left->left = newNode(4);
   root->left->right = newNode(5);
    cout << "traversal of binary tree is \n";
    printNodeTraversal(root);
    return 0;
}