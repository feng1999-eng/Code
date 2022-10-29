#include "iostream"
using namespace std;
typedef struct Node{
    int data;
    struct Node* next;
}linknode,*link;
                                                            curNode
                                                              |
void Bubble_list(linknode* head)//一般head是头节点，没有值，L->5->1->3->2->4->endNode
                                                            L->1->3->2->4->5
{                                                                         endNode
    linknode* curNode=head->next;
    linknode* endNode=nullptr;//用于表示当前已排序位置
    while(curNode->next!=endNode) //若curNode->next=endNOde表明已经冒泡完毕
    {
        linknode* nextNode=curNode->next;
        while(nextNode!=endNode)
        {
            if(curNode->data>nextNode->data)//又可能叫你换节点，需要知道更改位置之前的一个节点
            {
                int temp=curNode->data;
                curNode->data=nextNode->data;
                nextNode->data=temp;
            }
            curNode=nextNode;
            nextNode=nextNode->next;
        }
        endNode=curNode;//一次排序完成后，更新终点位置
        curNode=head->next;
    }
}
void Select_list(linknode* head)
{
    linknode* L=head;
    linknode* cur=head->next;
    linknode* small=cur;
    L->next=nullptr;

    while(cur)
    {
        linknode* cur_next=cur->next;
        while(cur_next)
        {

        }
    }
}
void Print(linknode* head)
{
    linknode* cur=head->next;
    while(cur)
    {
        cout<<cur->data<<" ";
        cur=cur->next;
    }
    cout<<endl;
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
    cout<<"冒泡排序前..."<<endl;
    Print(L);
    Bubble_list(L);
    cout<<"冒泡排序后..."<<endl;
    Print(L);
}