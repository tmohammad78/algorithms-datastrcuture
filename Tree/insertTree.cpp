#include <iostream>
#include <queue>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};
void inorder(Node* temp)
{
    if (temp == NULL)
        return;

    inorder(temp->left);
    cout << temp->data << ' ';
    inorder(temp->right);
}
Node* createNode(int data){
    Node* newNode = new Node();
    newNode->data = data;
    newNode->right=newNode->left = NULL;
    return newNode;
}
Node* insertNode(Node* root , int data){
    if (root == NULL) {
        root = createNode(data);
        return root;
    }
    queue<Node*> q;
    q.push(root);
    while(!q.empty()){
        Node* temp = q.front();
        q.pop();
        if(temp->left != NULL){
            q.push(temp->left);
        }else {
            temp->left = createNode(data);
            return root;
        }

        if(temp->right != NULL){
            q.push(temp->right);
        }else{
            temp->right = createNode(data);
            return root;
        }
    }
    return root;
}

int main(){
    Node* root = createNode(10);
    root->left = createNode(11);
    root->left->left = createNode(7);
    root->right = createNode(9);
    root->right->right = createNode(8);
    root->right->left = createNode(15);
    inorder(root);
    int key = 12;
    root = insertNode(root, key);
    cout << "Inorder traversal after insertion: ";
    inorder(root);
    cout << endl;
    return 0;
}