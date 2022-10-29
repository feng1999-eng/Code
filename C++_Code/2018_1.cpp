//
// Created by Administrator on 2022/10/17.
//

#include "stdio.h"
#include "malloc.h"
typedef struct Node
{
    int data;
    struct Node* next;
}linknode,*link;
void Reverse_L(link L)
{
    link p,q;
    p=L->next;
    L->next= nullptr;
    while(p!=nullptr)
    {
        q=p->next;
        p->next=L->next;
        L->next=p;
        p=q;
    }
}
void bubble_sort(Node* head)
{
    Node* tail = NULL;
    while(tail != head->next)
    {
        Node* pre = head;
        Node* cur = pre->next;
        while(cur != tail && cur->next != tail)
        {
            if( cur->data > cur->next->data )
            {
                //交换当前节点和后一个节点
                pre->next = cur->next;
                cur->next = cur->next->next;
                pre->next->next = cur;
            }
            pre = pre->next;
            cur = pre->next;
        }
        tail = cur;
    }
}
void PrintLinkNode(link L)
{
    link cur=L->next;
    while(cur!= nullptr) {
        printf("%d ", cur->data);
        cur=cur->next;
    }
    printf("\n");
}
int main()
{
    linknode* L=(link)malloc(sizeof(link));
    linknode* node1=(link)malloc(sizeof(link));
    linknode* node2=(link)malloc(sizeof(link));
    linknode* node3=(link)malloc(sizeof(link));
    linknode* node4=(link)malloc(sizeof(link));
    linknode* node5=(link)malloc(sizeof(link));
    node1->data=5;
    node2->data=2;
    node3->data=1;
    node4->data=4;
    node5->data=3;
    L->next=node1;
    node1->next=node2;
    node2->next=node3;
    node3->next=node4;
    node4->next=node5;
    node5->next= nullptr;
    PrintLinkNode(L);
    bubble_sort(L);
    PrintLinkNode(L);
}