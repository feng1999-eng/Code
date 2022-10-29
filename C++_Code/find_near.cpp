#include "stdio.h"
typedef struct NodeType
{
    int key;
    struct NodeType *leftChild,*rightChild;
}BSTNode,*BSTree;
BSTNode* Init()
{
    BSTNode* node1=new NodeType();
    BSTNode* node2=new NodeType();
    BSTNode* node3=new NodeType();
    BSTNode* node4=new NodeType();
    BSTNode* node5=new NodeType();
    BSTNode* node6=new NodeType();
    node1->key=5;
    node2->key=3;
    node3->key=7;
    node4->key=4;
    node5->key=6;
    node6->key=8;
    node1->leftChild=node2;
    node1->rightChild=node3;
    node2->leftChild= nullptr;
    node2->rightChild=node4;
    node3->leftChild=node5;
    node3->rightChild=node6;
    node4->leftChild= nullptr;
    node4->rightChild= nullptr;
    node5->leftChild= nullptr;
    node5->rightChild= nullptr;
    node6->leftChild= nullptr;
    node6->rightChild= nullptr;
    return node1;
}
BSTNode* find_near(BSTNode* root,BSTNode* A,BSTNode* B)
{
    if(root->key==A->key)
        return A;
    else if(root->key==B->key)
        return B;
    else if(root->key<A->key&&root->key<B->key)
    {
        return find_near(root->rightChild,A,B);
    }
    else if(root->key>A->key&&root->key>B->key)
    {
        return find_near(root->leftChild,A,B);
    }
    else
        return root;
}
int main()
{
    BSTNode* root=Init();
    BSTNode *A=new NodeType();
    BSTNode* B=new NodeType();
    A->key=4;
    A->leftChild= nullptr;
    A->rightChild= nullptr;
    B->key=8;
    B->leftChild= nullptr;
    B->rightChild= nullptr;
    BSTNode* res=new NodeType();
    res=find_near(root,A,B);
    printf("%d\n",res->key);
}