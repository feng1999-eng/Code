//
// Created by Administrator on 2022/10/17.
//

#include "stdio.h"
#include "malloc.h"
typedef struct LNode
{
    int data;
    struct LNode *next;
}LNode,*LinkList;
void impl(LinkList head,int k)
{
    int count=0;
    LinkList p,toReverseHead;
    p=head->next;
    toReverseHead=head;
    while(p)
    {
        if(count<k)  //前k个不管
            count++;
        else
            toReverseHead=toReverseHead->next;
        p=p->next;
    }
    p=toReverseHead->next;
    toReverseHead->next= nullptr;
    toReverseHead=p;
    while(toReverseHead)
    {
        p=toReverseHead->next;
        toReverseHead->next=head->next;
        head->next=toReverseHead;
        toReverseHead=p;
    }
}