#include "iostream"
using namespace std;
typedef struct Node{
    int data;
    struct Node* next;
}linknode,*link;
                                                            curNode
                                                              |
void Bubble_list(linknode* head)//һ��head��ͷ�ڵ㣬û��ֵ��L->5->1->3->2->4->endNode
                                                            L->1->3->2->4->5
{                                                                         endNode
    linknode* curNode=head->next;
    linknode* endNode=nullptr;//���ڱ�ʾ��ǰ������λ��
    while(curNode->next!=endNode) //��curNode->next=endNOde�����Ѿ�ð�����
    {
        linknode* nextNode=curNode->next;
        while(nextNode!=endNode)
        {
            if(curNode->data>nextNode->data)//�ֿ��ܽ��㻻�ڵ㣬��Ҫ֪������λ��֮ǰ��һ���ڵ�
            {
                int temp=curNode->data;
                curNode->data=nextNode->data;
                nextNode->data=temp;
            }
            curNode=nextNode;
            nextNode=nextNode->next;
        }
        endNode=curNode;//һ��������ɺ󣬸����յ�λ��
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
    cout<<"ð������ǰ..."<<endl;
    Print(L);
    Bubble_list(L);
    cout<<"ð�������..."<<endl;
    Print(L);
}